import csv


def get_campaigns(filename):
    with open(filename) as csvfile:
        return list(csv.DictReader(csvfile))


def order_by_payout(filename):
    campaigns = get_campaigns(filename)
    campaigns.sort(key=lambda row: row['payout'], reverse=True)
    list_of_payout = [int(row['id']) for row in campaigns]
    return list_of_payout


def order_by_total_payout(filename):
    """
    >>> total_payout = payout * installs
    """
    campaigns = get_campaigns(filename)
    campaigns.sort(key=lambda x: float(x['payout'].replace(',', '.')) * int(x['installs']),
                   reverse=True)
    list_of_total = [int(row['id']) for row in campaigns]
    return list_of_total


def order_by_cr(filename):
    """
    >>> cr = impressions / installs
    """
    campaigns = get_campaigns(filename)
    campaigns.sort(key=lambda x: float(x['impressions']) / float(x['installs']),
                   reverse=False)
    list_of_cr = [int(row['id']) for row in campaigns]
    return list_of_cr


if __name__ == "__main__":
    payout_order = [17, 14, 22, 7, 11, 15, 23, 13, 18, 12, 6, 1, 3,
                    10, 25, 24, 21, 16, 20, 5, 4, 8, 9, 19, 2]
    total_payout_order = [15, 11, 18, 7, 14, 21, 3, 6, 25, 13, 16, 5,
                          24, 20, 17, 23, 1, 10, 8, 9, 19, 12, 4, 22,
                          2]
    cr_order = [11, 15, 18, 25, 21, 7, 8, 24, 6, 14, 3, 9, 5, 16,
                19, 10, 20, 2, 13, 4, 17, 1, 23, 12, 22]
    assert order_by_payout('campaigns.csv') == payout_order
    assert order_by_total_payout('campaigns.csv') == total_payout_order
    assert order_by_cr('campaigns.csv') == cr_order
