from flask import Blueprint, request, jsonify
from delivery.main import Thalia
from delivery.convert import show_create_api_v1, show_all_api_v1, show_wid_api_v1, show_section_api_v1, \
    seating_with_sid_api_v1, show_donation_create_api_v1, show_donation_api_v1

show = Blueprint('show', __name__)
seating = Blueprint('seating', __name__)
ticket = Blueprint('ticket', __name__)
search = Blueprint('search', __name__)
report = Blueprint('report', __name__)
order = Blueprint('order', __name__)

main = Thalia()


@show.route('/shows', methods=['GET', 'POST'])
def show_req_all():
    if request.method == 'POST':
        content = request.get_json()
        showinfo = content['show_info']
        seat = content['seating_info']
        s = main.post_show(show_info=showinfo, seating=seat)
        return jsonify(show_create_api_v1(s))
    else:
        return jsonify(show_all_api_v1(main.get_shows()))


@show.route('/shows/<wid>', methods=['GET', 'PUT'])
def req_view(wid):
    if request.method == 'PUT':
        content = request.get_json()
        main.put_show(wid=wid, show_info=content['show_info'], seating=content['seating_info'])
        return ''
    else:
        return jsonify(show_wid_api_v1(main.get_shows(wid)))


@show.route('/shows/<wid>/sections', methods=['GET'])
def req_show_section(wid):
    return jsonify(show_section_api_v1(main.get_shows(wid)))


@show.route('/shows/<wid>/sections/<sid>', methods=['GET'])
def req_show_section_by_sid(wid, sid):
    show_returned, section = main.get_show_section_by_id(wid=wid, sid=sid)
    return jsonify(seating_with_sid_api_v1(show_returned, section))


@show.route('/shows/<wid>/donations/<did>', methods=['GET'])
def req_show_donation(wid, did):
    return jsonify(show_donation_api_v1(main.get_donations_by_id(wid, did)))


@show.route('/shows/<wid>/donations', methods=['POST'])
def req_all_donations(wid):
    content = request.get_json()
    return jsonify(show_donation_create_api_v1(main.post_get_donations(
        patron=content['patron_info'], amount=content['count'], wid=wid)))


""" SEATING CONTROLLER """


@seating.route('/seating', methods=['GET'])
def seating_view_all():
    if sorted(['show', 'section', 'count']) == sorted(request.args.keys()):
        wid = request.args['show']
        sid = request.args['section']
        count = request.args['count']
        start_seat = None
        return jsonify(main.show_seats_request(wid=wid, sid=sid, count=count, start_id=start_seat))
    elif sorted(['show', 'section', 'count', 'starting_seat_id']) == sorted(request.args.keys()):
        wid = request.args['show']
        sid = request.args['section']
        count = request.args['count']
        start_seat = request.args['starting_seat_id']
        return jsonify(main.show_seats_request(wid=wid, sid=sid, count=count, start_id=start_seat))
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
    return jsonify(list(map(lambda x: x.to_dict(), main.get_reports())))


@report.route('/reports/<string:mrid>', methods=['GET'])
def req_report(mrid):
    # ?show={wid} | ?start_date=YYYYMMDD&end_date=YYYYMMDD
    if list(request.args.keys()) == ['show']:
        wid = request.args.get('show')
        if not isinstance(wid, list):
            wid = [wid]
        return jsonify(main.get_reports(mrid=mrid, show=wid).report())
    elif sorted(request.args.keys()) == sorted(['start_date', 'end_date']):
        start = request.args.get('start_date', type=str)
        end = request.args.get('end_date', type=str)
        return jsonify(main.get_reports(mrid=mrid, start=start, end=end).report())
    return jsonify(main.get_reports(mrid=mrid).report())


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
    elif ['end_date', 'start_date'] == sorted(request.args.keys()):
        start = request.args.get('start_date', type=str)
        end = request.args.get('end_date', type=str)
        return jsonify(main.order_by_date(start=start, end=end))
    else:
        return jsonify(main.get_orders())


@order.route('/orders/<oid>', methods=['GET'])
def req_view(oid):
    return jsonify(main.get_orders(oid))
