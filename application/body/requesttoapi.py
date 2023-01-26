import aiohttp
import json
from application.logging.loggers import get_core_logger
import pandas as pd

logger = get_core_logger()


def parse_json_and_print(result):
    result = json.loads(result)
    data = result["people"]
    return f"The count of astronauts in space at this moment is  {len(data)} people"


async def get_astronaut_from_json() -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get("http://api.open-notify.org/astros.json") as response:
            result = await response.text()
            return parse_json_and_print(result)


"""File csv download #https://drive.google.com/file/d/13nk_FYpcayUck2Ctrela5Tjt9JQbjznt/view"""


def get_csv_file_data_and_calculate(link: str = None) -> dict:
    csv_data = pd.read_csv(link)
    csv_data.head()
    # csv_data.to_csv(path_to_file)
    avr_height = csv_data["Height(Inches)"].mean()
    sm_height = round(avr_height * 2.54, 2)
    avr_weight = csv_data["Weight(Pounds)"].mean()
    kg_weight = round(avr_weight * 0.45, 2)
    return {"average_height": sm_height, "average_weight": kg_weight}
