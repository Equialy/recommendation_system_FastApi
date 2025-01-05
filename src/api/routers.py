from src.api.purchases import router as router_purchases
from src.api.users import router as router_users
from src.api.items import router as router_items
from src.api.recommendations import router as router_recommendations


all_routers = [router_purchases, router_users,router_items,router_recommendations]