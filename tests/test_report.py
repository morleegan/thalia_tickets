from thalia.report import Report, RevenueReport, DonatedReport, OccupancyReport


def test_create_report():
    rep = Report()
    assert isinstance(rep, Report)
    rep = RevenueReport()
    assert isinstance(rep, RevenueReport)
    rep = OccupancyReport()
    assert isinstance(rep, OccupancyReport)
    rep = DonatedReport()
    assert isinstance(rep, DonatedReport)


if __name__ == '__main__':
    test_create_report()