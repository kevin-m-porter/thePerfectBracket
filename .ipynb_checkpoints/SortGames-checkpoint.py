{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "68238133",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Processing 2015\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████████████████████████████████████████████████████████████████████████████| 63/63 [00:31<00:00,  2.02it/s]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Processing 2016\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████████████████████████████████████████████████████████████████████████████| 63/63 [00:31<00:00,  1.99it/s]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Processing 2017\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████████████████████████████████████████████████████████████████████████████| 63/63 [00:30<00:00,  2.04it/s]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Processing 2018\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████████████████████████████████████████████████████████████████████████████| 63/63 [00:37<00:00,  1.69it/s]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Processing 2019\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████████████████████████████████████████████████████████████████████████████| 63/63 [00:36<00:00,  1.72it/s]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Processing 2021\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████████████████████████████████████████████████████████████████████████████| 63/63 [00:35<00:00,  1.78it/s]\n"
     ]
    }
   ],
   "source": [
    "from sportsipy.ncaab.schedule import Schedule\n",
    "import pandas as pd\n",
    "import os\n",
    "from datetime import datetime\n",
    "from dateutil import parser\n",
    "from tqdm import tqdm\n",
    "\n",
    "\n",
    "def WriteSortedGames(tourneyGames,Year)\n",
    "\n",
    "    # This file has the coversions between bart torvick and sports reference\n",
    "    Translator = pd.read_csv(os.path.join('DATA','Translator.csv'),header=None)\n",
    "\n",
    "\n",
    "    for ind,(games_file,year) in enumerate(zip(tourneyGames,Year)):\n",
    "\n",
    "        print(f' Processing {year}')\n",
    "\n",
    "        # Empty dataframe with our columns\n",
    "        df = pd.DataFrame(columns = ['Datetime' , 'Winner', 'Loser'])\n",
    "\n",
    "        # Read the raw game data\n",
    "        Games = pd.read_csv(os.path.join('DATA',games_file),header=None)\n",
    "\n",
    "        # Loop through all relevent games\n",
    "        for indexs, game in tqdm(Games[4:].iterrows(),total=63): # games 0-3 playin games\n",
    "\n",
    "\n",
    "            winner= game[1]      \n",
    "            loser = game[2]\n",
    "\n",
    "            # Translate team to sports ref\n",
    "            winner_trans = Translator[Translator[1].str.fullmatch(winner)]        \n",
    "            winner_ref = winner_trans.iloc[0][0]\n",
    "\n",
    "            # Convert date to datetime\n",
    "            datetime_object = datetime.strptime(game[0],  '%m/%d/%Y')\n",
    "\n",
    "            # Grab schedule data that includes tip times\n",
    "            schedule = Schedule(winner_ref,year=year)\n",
    "\n",
    "\n",
    "            matched = False\n",
    "            for gameref in schedule:\n",
    "                if gameref.type =='NCAA' and datetime_object==parser.parse(gameref.date):\n",
    "                    matched= True\n",
    "                    t = [parser.parse(game[0]+' '+gameref.time),winner,loser]\n",
    "                    df.loc[len(df)] = t  \n",
    "\n",
    "            if not matched:\n",
    "                print(f'{game[0]} , Winner - {winner}, Loser - {loser} - No match??')\n",
    "\n",
    "        # After all games are added sort by datetime\n",
    "        df = df.sort_values(by='Datetime', ascending=True)\n",
    "\n",
    "        # Write to file\n",
    "        df.to_csv(os.path.join('DATA',f'GamesSorted_{year}.csv'),index=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
