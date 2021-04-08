# MachineCodingMandi

## Project Setup

Clone the repository

```
git clone https://github.com/shikhar1996/MachineCodingMandi.git
```

Run main.py
```
python3 main.py
```

###Access the API and custom test cases

Update data pass list of strings in the following format
'Maharashtra, Nagpur, ABC, Tomato, Hybrid, 2021-04-07, 400'
```
from controllers.data_util import update_data
update_date(data)
```
Access APIs

1. Given state, district and crop, for all mandis in given district, for all crop varieties, show latest price & date (Sorted by latest date)
```
from views.api import get_latest_price
get_latest_price()
```

2. Given state, district, mandi, crop, crop variety, show price trend of x points in last y days
E.g Last 7 latest prices in last 15 days
```
from views.api import get_price_trend
get_price_trend()
```
