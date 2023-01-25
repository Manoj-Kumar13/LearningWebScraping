from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.select_place_to_go("guwahati")
    bot.select_dates('2023-01-25','2023-01-28')
    bot.select_adults(adults=1)
    bot.apply_filtration()