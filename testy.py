from main import Harvestor
from time import sleep

Harvestor().startHarvestor('https://www.johnelliott.co/pages/lebron-james-x-john-elliott-nikelab-icon-friends-family-giveaway',"186e8b93b5bd710a5b9839bb1749e941" )
sleep(60)
Harvestor().getTokens()