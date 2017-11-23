from flask import Blueprint, request, jsonify
from delivery.main import Emulate
from helpers.helper import Helper

show = Blueprint('show', __name__)
seating = Blueprint('seating', __name__)
ticket = Blueprint('ticket', __name__)
search = Blueprint('search', __name__)
report = Blueprint('report', __name__)
order = Blueprint('order', __name__)

main = Emulate()


@show.route('/shows', methods=['GET', 'POST'])
def show_req_all():
    if request.method == 'POST':
        content = request.get_json()
        showinfo = content['show_info']
        seating = content['seating_info']
        show = main.post_show(show_info=showinfo, seating=seating)
        return jsonify(show)
    else:
        return jsonify(main.get_shows())


@show.route('/shows/<wid>', methods=['GET', 'PUT'])
def req_view(wid):
    if request.method == 'PUT':
        content = request.get_json()
        main.put_show(wid=wid, show_info=content['show_info'], seating=content['seating_info'])
        return ''
    else:
        s = main.get_shows(wid)
        s['seating_info'] = list(map(lambda x: Helper.delete_keys(x, ['section_name', 'seating']), s['seating_info']))
        return jsonify(s)


@show.route('/shows/<wid>/sections', methods=['GET'])
def req_show_section(wid):
    return jsonify(main.get_show_section(wid))


@show.route('/shows/<wid>/sections/<sid>', methods=['GET'])
def req_show_section_by_sid(wid, sid):
    return jsonify(main.get_show_section_by_id(wid=wid, sid=sid))


@show.route('/shows/<wid>/donations/<did>', methods=['GET'])
def req_show_donation(wid, did):
    return jsonify(main.get_donations_by_id(wid, did))


@show.route('/shows/<wid>/donations', methods=['POST'])
def req_all_donations(wid):
    content = request.get_json()
    return jsonify(main.post_get_donations(patron=content['patron_info'], amount=content['count'], wid=wid))


""" SEATING CONTROLLER """


@seating.route('/seating', methods=['GET'])
def seating_view_all():
    if sorted(['show', 'section', 'count']) == sorted(request.args.keys()):
        wid = request.args['show']
        sid = request.args['section']
        count = request.args['count']
        # return jsonify(main.show_seats_request(wid=wid, sid=sid, count=count))
        return jsonify(None)
    return jsonify(main.get_seating())


@seating.route('/seating/<sid>', methods=['GET'])
def req_view(sid):
    s = main.get_seating(sid=sid)
    for r in s['seating']:
        r['seats'] = sorted(list(map(lambda x: x['seat'], r['seats'])))
    return jsonify(s)


""" Ticket Controller """


@ticket.route('/tickets/<tid>', methods=['POST', 'GET'])
def req_view_t(tid):
    if request.method == 'POST':
        content = request.get_json()
        return jsonify(main.post_ticket(tid, content['status']))
    return jsonify(main.get_tickets(tid))


@ticket.route('/tickets/donations', methods=['POST'])
def req_ticket_donations():
    content = request.get_json()
    tid = content['tickets']
    return jsonify(main.post_donate(tid_list=tid))


""" search controller """


@search.route('/search', methods=['GET'])
def req_report():
    # search?topic=topicword&key=keyword
    topic = request.args.get('topic', type=str)
    key = request.args.get('key', type=str)
    return jsonify(main.search(topic, key))


""" Report Controller """


@report.route('/reports', methods=['GET'])
def req_view():
    return jsonify(main.get_reports())


# @report.route('/reports/<mrid>', methods=['GET'])
# def req_report(mrid):
#     # ?show={wid} | ?start_date=YYYYMMDD&end_date=YYYYMMDD
#     wid = request.args.get('show', type=int)
#     start = request.args.get('start_date', type=str)    # TODO: will have to parse
#     end = request.args.get('end_date', type=str)
#     return "start: " + start
#

""" Order Controller """


@order.route('/orders', methods=['GET', 'POST'])
def req_view_all():
    if request.method == 'POST':
        content = request.get_json()
        wid = content['wid']
        sid = content['sid']
        seats = content['seats']
        patron = content['patron_info']
        return jsonify(main.post_order(wid, sid, seats, patron))
    else:
        return jsonify(main.get_orders())


@order.route('/orders/<oid>', methods=['GET'])
def req_view(oid):
    return jsonify(main.get_orders(oid))


# @order.route('/orders', methods=['GET'])
# def req_order_by_dates():
#     # ?start_date = YYYYMMDD & end_date = YYYYMMDD
#     start = request.args.get('start_date', type=str)    # TODO: will have to parse
#     end = request.args.get('end_date', type=str)
#     return "start: " + start
#

