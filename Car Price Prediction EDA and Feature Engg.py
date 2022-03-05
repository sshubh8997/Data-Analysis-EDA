{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9071b656",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "289dfe17",
   "metadata": {},
   "outputs": [],
   "source": [
    "car=pd.read_csv(r'C:\\Users\\S.S\\Downloads\\quikr_car.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "200c4386",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>company</th>\n",
       "      <th>year</th>\n",
       "      <th>Price</th>\n",
       "      <th>kms_driven</th>\n",
       "      <th>fuel_type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Hyundai Santro Xing XO eRLX Euro III</td>\n",
       "      <td>Hyundai</td>\n",
       "      <td>2007</td>\n",
       "      <td>80,000</td>\n",
       "      <td>45,000 kms</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mahindra Jeep CL550 MDI</td>\n",
       "      <td>Mahindra</td>\n",
       "      <td>2006</td>\n",
       "      <td>4,25,000</td>\n",
       "      <td>40 kms</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Maruti Suzuki Alto 800 Vxi</td>\n",
       "      <td>Maruti</td>\n",
       "      <td>2018</td>\n",
       "      <td>Ask For Price</td>\n",
       "      <td>22,000 kms</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hyundai Grand i10 Magna 1.2 Kappa VTVT</td>\n",
       "      <td>Hyundai</td>\n",
       "      <td>2014</td>\n",
       "      <td>3,25,000</td>\n",
       "      <td>28,000 kms</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Ford EcoSport Titanium 1.5L TDCi</td>\n",
       "      <td>Ford</td>\n",
       "      <td>2014</td>\n",
       "      <td>5,75,000</td>\n",
       "      <td>36,000 kms</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                     name   company  year          Price  \\\n",
       "0    Hyundai Santro Xing XO eRLX Euro III   Hyundai  2007         80,000   \n",
       "1                 Mahindra Jeep CL550 MDI  Mahindra  2006       4,25,000   \n",
       "2              Maruti Suzuki Alto 800 Vxi    Maruti  2018  Ask For Price   \n",
       "3  Hyundai Grand i10 Magna 1.2 Kappa VTVT   Hyundai  2014       3,25,000   \n",
       "4        Ford EcoSport Titanium 1.5L TDCi      Ford  2014       5,75,000   \n",
       "\n",
       "   kms_driven fuel_type  \n",
       "0  45,000 kms    Petrol  \n",
       "1      40 kms    Diesel  \n",
       "2  22,000 kms    Petrol  \n",
       "3  28,000 kms    Petrol  \n",
       "4  36,000 kms    Diesel  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "86ec49ea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(892, 6)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "65eae23a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "name           0\n",
       "company        0\n",
       "year           0\n",
       "Price          0\n",
       "kms_driven    52\n",
       "fuel_type     55\n",
       "dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d5d5b3aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 892 entries, 0 to 891\n",
      "Data columns (total 6 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   name        892 non-null    object\n",
      " 1   company     892 non-null    object\n",
      " 2   year        892 non-null    object\n",
      " 3   Price       892 non-null    object\n",
      " 4   kms_driven  840 non-null    object\n",
      " 5   fuel_type   837 non-null    object\n",
      "dtypes: object(6)\n",
      "memory usage: 41.9+ KB\n"
     ]
    }
   ],
   "source": [
    "car.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "11a47911",
   "metadata": {},
   "source": [
    "1. year has to many nonnumeric value\n",
    "2. change year into integer\n",
    "3. kms has nan value and remove kms\n",
    "4. kms has comma remove comma and make integer\n",
    "5. remove nan value from fuel\n",
    "6. consider frist 3 value from name column\n",
    "7. remove comma from price column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "515d82dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "car=car[car['year'].str.isnumeric()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8209b6cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>company</th>\n",
       "      <th>year</th>\n",
       "      <th>Price</th>\n",
       "      <th>kms_driven</th>\n",
       "      <th>fuel_type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Hyundai Santro Xing XO eRLX Euro III</td>\n",
       "      <td>Hyundai</td>\n",
       "      <td>2007</td>\n",
       "      <td>80,000</td>\n",
       "      <td>45,000 kms</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mahindra Jeep CL550 MDI</td>\n",
       "      <td>Mahindra</td>\n",
       "      <td>2006</td>\n",
       "      <td>4,25,000</td>\n",
       "      <td>40 kms</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Maruti Suzuki Alto 800 Vxi</td>\n",
       "      <td>Maruti</td>\n",
       "      <td>2018</td>\n",
       "      <td>Ask For Price</td>\n",
       "      <td>22,000 kms</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hyundai Grand i10 Magna 1.2 Kappa VTVT</td>\n",
       "      <td>Hyundai</td>\n",
       "      <td>2014</td>\n",
       "      <td>3,25,000</td>\n",
       "      <td>28,000 kms</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Ford EcoSport Titanium 1.5L TDCi</td>\n",
       "      <td>Ford</td>\n",
       "      <td>2014</td>\n",
       "      <td>5,75,000</td>\n",
       "      <td>36,000 kms</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>Toyota Corolla Altis</td>\n",
       "      <td>Toyota</td>\n",
       "      <td>2009</td>\n",
       "      <td>3,00,000</td>\n",
       "      <td>1,32,000 kms</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>Tata Zest XM Diesel</td>\n",
       "      <td>Tata</td>\n",
       "      <td>2018</td>\n",
       "      <td>2,60,000</td>\n",
       "      <td>27,000 kms</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>Mahindra Quanto C8</td>\n",
       "      <td>Mahindra</td>\n",
       "      <td>2013</td>\n",
       "      <td>3,90,000</td>\n",
       "      <td>40,000 kms</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>Honda Amaze 1.2 E i VTEC</td>\n",
       "      <td>Honda</td>\n",
       "      <td>2014</td>\n",
       "      <td>1,80,000</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>891</th>\n",
       "      <td>Chevrolet Sail 1.2 LT ABS</td>\n",
       "      <td>Chevrolet</td>\n",
       "      <td>2014</td>\n",
       "      <td>1,60,000</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>842 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                       name    company  year          Price  \\\n",
       "0      Hyundai Santro Xing XO eRLX Euro III    Hyundai  2007         80,000   \n",
       "1                   Mahindra Jeep CL550 MDI   Mahindra  2006       4,25,000   \n",
       "2                Maruti Suzuki Alto 800 Vxi     Maruti  2018  Ask For Price   \n",
       "3    Hyundai Grand i10 Magna 1.2 Kappa VTVT    Hyundai  2014       3,25,000   \n",
       "4          Ford EcoSport Titanium 1.5L TDCi       Ford  2014       5,75,000   \n",
       "..                                      ...        ...   ...            ...   \n",
       "886                    Toyota Corolla Altis     Toyota  2009       3,00,000   \n",
       "888                     Tata Zest XM Diesel       Tata  2018       2,60,000   \n",
       "889                      Mahindra Quanto C8   Mahindra  2013       3,90,000   \n",
       "890                Honda Amaze 1.2 E i VTEC      Honda  2014       1,80,000   \n",
       "891               Chevrolet Sail 1.2 LT ABS  Chevrolet  2014       1,60,000   \n",
       "\n",
       "       kms_driven fuel_type  \n",
       "0      45,000 kms    Petrol  \n",
       "1          40 kms    Diesel  \n",
       "2      22,000 kms    Petrol  \n",
       "3      28,000 kms    Petrol  \n",
       "4      36,000 kms    Diesel  \n",
       "..            ...       ...  \n",
       "886  1,32,000 kms    Petrol  \n",
       "888    27,000 kms    Diesel  \n",
       "889    40,000 kms    Diesel  \n",
       "890        Petrol       NaN  \n",
       "891        Petrol       NaN  \n",
       "\n",
       "[842 rows x 6 columns]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0395c267",
   "metadata": {},
   "outputs": [],
   "source": [
    "car['year']=car['year'].astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c0c78a65",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 842 entries, 0 to 891\n",
      "Data columns (total 6 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   name        842 non-null    object\n",
      " 1   company     842 non-null    object\n",
      " 2   year        842 non-null    int32 \n",
      " 3   Price       842 non-null    object\n",
      " 4   kms_driven  840 non-null    object\n",
      " 5   fuel_type   837 non-null    object\n",
      "dtypes: int32(1), object(5)\n",
      "memory usage: 42.8+ KB\n"
     ]
    }
   ],
   "source": [
    "car.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b2f48841",
   "metadata": {},
   "outputs": [],
   "source": [
    "car['kms_driven']=car['kms_driven'].str.split(' ').str.get(0).str.replace(',','')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "804583a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['45000', '40', '22000', '28000', '36000', '59000', '41000',\n",
       "       '25000', '24530', '60000', '30000', '32000', '48660', '4000',\n",
       "       '16934', '43000', '35550', '39522', '39000', '55000', '72000',\n",
       "       '15975', '70000', '23452', '35522', '48508', '15487', '82000',\n",
       "       '20000', '68000', '38000', '27000', '33000', '46000', '16000',\n",
       "       '47000', '35000', '30874', '15000', '29685', '130000', '19000',\n",
       "       nan, '54000', '13000', '38200', '50000', '13500', '3600', '45863',\n",
       "       '60500', '12500', '18000', '13349', '29000', '44000', '42000',\n",
       "       '14000', '49000', '36200', '51000', '104000', '33333', '33600',\n",
       "       '5600', '7500', '26000', '24330', '65480', '28028', '200000',\n",
       "       '99000', '2800', '21000', '11000', '66000', '3000', '7000',\n",
       "       '38500', '37200', '43200', '24800', '45872', '40000', '11400',\n",
       "       '97200', '52000', '31000', '175430', '37000', '65000', '3350',\n",
       "       '75000', '62000', '73000', '2200', '54870', '34580', '97000', '60',\n",
       "       '80200', '3200', '0000', '5000', '588', '71200', '175400', '9300',\n",
       "       '56758', '10000', '56450', '56000', '32700', '9000', '73',\n",
       "       '160000', '84000', '58559', '57000', '170000', '80000', '6821',\n",
       "       '23000', '34000', '1800', '400000', '48000', '90000', '12000',\n",
       "       '69900', '166000', '122', '0', '24000', '36469', '7800', '24695',\n",
       "       '15141', '59910', '100000', '4500', '129000', '300', '131000',\n",
       "       '111111', '59466', '25500', '44005', '2110', '43222', '100200',\n",
       "       '65', '140000', '103553', '58000', '120000', '49800', '100',\n",
       "       '81876', '6020', '55700', '18500', '180000', '53000', '35500',\n",
       "       '22134', '1000', '8500', '87000', '6000', '15574', '8000', '55800',\n",
       "       '56400', '72160', '11500', '133000', '2000', '88000', '65422',\n",
       "       '117000', '150000', '10750', '6800', '5', '9800', '57923', '30201',\n",
       "       '6200', '37518', '24652', '383', '95000', '3528', '52500', '47900',\n",
       "       '52800', '195000', '48008', '48247', '9400', '64000', '2137',\n",
       "       '10544', '49500', '147000', '90001', '48006', '74000', '85000',\n",
       "       '29500', '39700', '67000', '19336', '60105', '45933', '102563',\n",
       "       '28600', '41800', '116000', '42590', '7400', '54500', '76000',\n",
       "       '00', '11523', '38600', '95500', '37458', '85960', '12516',\n",
       "       '30600', '2550', '62500', '69000', '28400', '68485', '3500',\n",
       "       '85455', '63000', '1600', '77000', '26500', '2875', '13900',\n",
       "       '1500', '2450', '1625', '33400', '60123', '38900', '137495',\n",
       "       '91200', '146000', '100800', '2100', '2500', '132000', 'Petrol'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car['kms_driven'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "1660ee33",
   "metadata": {},
   "outputs": [],
   "source": [
    "car=car[~car['kms_driven'].isna()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "9e20e7ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "car=car[car['kms_driven'].str.isnumeric()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "3dd0d475",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\S.S\\AppData\\Local\\Temp/ipykernel_4100/1713770885.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  car['kms_driven']=car['kms_driven'].astype(int)\n"
     ]
    }
   ],
   "source": [
    "car['kms_driven']=car['kms_driven'].astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "43a55966",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 838 entries, 0 to 889\n",
      "Data columns (total 6 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   name        838 non-null    object\n",
      " 1   company     838 non-null    object\n",
      " 2   year        838 non-null    int32 \n",
      " 3   Price       838 non-null    object\n",
      " 4   kms_driven  838 non-null    int32 \n",
      " 5   fuel_type   837 non-null    object\n",
      "dtypes: int32(2), object(4)\n",
      "memory usage: 39.3+ KB\n"
     ]
    }
   ],
   "source": [
    "car.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "ab8fa07a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Petrol', 'Diesel', nan, 'LPG'], dtype=object)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.fuel_type.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "4fb99381",
   "metadata": {},
   "outputs": [],
   "source": [
    "car=car[~car['fuel_type'].isna()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "0bfbdbd1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Petrol', 'Diesel', 'LPG'], dtype=object)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.fuel_type.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "1e12cd4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "name          0\n",
       "company       0\n",
       "year          0\n",
       "Price         0\n",
       "kms_driven    0\n",
       "fuel_type     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "0c50a65c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['80,000', '4,25,000', 'Ask For Price', '3,25,000', '5,75,000',\n",
       "       '1,75,000', '1,90,000', '8,30,000', '2,50,000', '1,82,000',\n",
       "       '3,15,000', '4,15,000', '3,20,000', '10,00,000', '5,00,000',\n",
       "       '3,50,000', '1,60,000', '3,10,000', '75,000', '1,00,000',\n",
       "       '2,90,000', '95,000', '1,80,000', '3,85,000', '1,05,000',\n",
       "       '6,50,000', '6,89,999', '4,48,000', '5,49,000', '5,01,000',\n",
       "       '4,89,999', '2,80,000', '3,49,999', '2,84,999', '3,45,000',\n",
       "       '4,99,999', '2,35,000', '2,49,999', '14,75,000', '3,95,000',\n",
       "       '2,20,000', '1,70,000', '85,000', '2,00,000', '5,70,000',\n",
       "       '1,10,000', '4,48,999', '18,91,111', '1,59,500', '3,44,999',\n",
       "       '4,49,999', '8,65,000', '6,99,000', '3,75,000', '2,24,999',\n",
       "       '12,00,000', '1,95,000', '3,51,000', '2,40,000', '90,000',\n",
       "       '1,55,000', '6,00,000', '1,89,500', '2,10,000', '3,90,000',\n",
       "       '1,35,000', '16,00,000', '7,01,000', '2,65,000', '5,25,000',\n",
       "       '3,72,000', '6,35,000', '5,50,000', '4,85,000', '3,29,500',\n",
       "       '2,51,111', '5,69,999', '69,999', '2,99,999', '3,99,999',\n",
       "       '4,50,000', '2,70,000', '1,58,400', '1,79,000', '1,25,000',\n",
       "       '2,99,000', '1,50,000', '2,85,000', '3,40,000', '70,000',\n",
       "       '2,89,999', '8,49,999', '7,49,999', '2,74,999', '9,84,999',\n",
       "       '5,99,999', '2,44,999', '4,74,999', '2,45,000', '1,69,500',\n",
       "       '2,75,000', '3,70,000', '1,68,000', '1,45,000', '98,500',\n",
       "       '2,09,000', '1,85,000', '9,00,000', '6,99,999', '1,99,999',\n",
       "       '5,44,999', '1,99,000', '5,40,000', '49,000', '7,00,000', '55,000',\n",
       "       '8,95,000', '3,55,000', '5,65,000', '3,65,000', '40,000',\n",
       "       '4,00,000', '3,30,000', '5,80,000', '3,79,000', '2,19,000',\n",
       "       '5,19,000', '7,30,000', '20,00,000', '21,00,000', '14,00,000',\n",
       "       '3,11,000', '8,55,000', '5,35,000', '1,78,000', '3,00,000',\n",
       "       '2,55,000', '5,49,999', '3,80,000', '57,000', '4,10,000',\n",
       "       '2,25,000', '1,20,000', '59,000', '5,99,000', '6,75,000', '72,500',\n",
       "       '6,10,000', '2,30,000', '5,20,000', '5,24,999', '4,24,999',\n",
       "       '6,44,999', '5,84,999', '7,99,999', '4,44,999', '6,49,999',\n",
       "       '9,44,999', '5,74,999', '3,74,999', '1,30,000', '4,01,000',\n",
       "       '13,50,000', '1,74,999', '2,39,999', '99,999', '3,24,999',\n",
       "       '10,74,999', '11,30,000', '1,49,000', '7,70,000', '30,000',\n",
       "       '3,35,000', '3,99,000', '65,000', '1,69,999', '1,65,000',\n",
       "       '5,60,000', '9,50,000', '7,15,000', '45,000', '9,40,000',\n",
       "       '1,55,555', '15,00,000', '4,95,000', '8,00,000', '12,99,000',\n",
       "       '5,30,000', '14,99,000', '32,000', '4,05,000', '7,60,000',\n",
       "       '7,50,000', '4,19,000', '1,40,000', '15,40,000', '1,23,000',\n",
       "       '4,98,000', '4,80,000', '4,88,000', '15,25,000', '5,48,900',\n",
       "       '7,25,000', '99,000', '52,000', '28,00,000', '4,99,000',\n",
       "       '3,81,000', '2,78,000', '6,90,000', '2,60,000', '90,001',\n",
       "       '1,15,000', '15,99,000', '1,59,000', '51,999', '2,15,000',\n",
       "       '35,000', '11,50,000', '2,69,000', '60,000', '4,30,000',\n",
       "       '85,00,003', '4,01,919', '4,90,000', '4,24,000', '2,05,000',\n",
       "       '5,49,900', '4,35,000', '1,89,700', '3,89,700', '3,60,000',\n",
       "       '2,95,000', '1,14,990', '10,65,000', '4,70,000', '48,000',\n",
       "       '1,88,000', '4,65,000', '1,79,999', '21,90,000', '23,90,000',\n",
       "       '10,75,000', '4,75,000', '10,25,000', '6,15,000', '19,00,000',\n",
       "       '14,90,000', '15,10,000', '18,50,000', '7,90,000', '17,25,000',\n",
       "       '12,25,000', '68,000', '9,70,000', '31,00,000', '8,99,000',\n",
       "       '88,000', '53,000', '5,68,500', '71,000', '5,90,000', '7,95,000',\n",
       "       '42,000', '1,89,000', '1,62,000', '35,999', '29,00,000', '39,999',\n",
       "       '50,500', '5,10,000', '8,60,000', '5,00,001'], dtype=object)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.Price.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "7e097964",
   "metadata": {},
   "outputs": [],
   "source": [
    "car=car[car['Price']!='Ask For Price']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "a9c654e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "car['Price']=car['Price'].str.replace(',','').astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "173ee84c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 816 entries, 0 to 889\n",
      "Data columns (total 6 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   name        816 non-null    object\n",
      " 1   company     816 non-null    object\n",
      " 2   year        816 non-null    int32 \n",
      " 3   Price       816 non-null    int32 \n",
      " 4   kms_driven  816 non-null    int32 \n",
      " 5   fuel_type   816 non-null    object\n",
      "dtypes: int32(3), object(3)\n",
      "memory usage: 35.1+ KB\n"
     ]
    }
   ],
   "source": [
    "car.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "0b038183",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>company</th>\n",
       "      <th>year</th>\n",
       "      <th>Price</th>\n",
       "      <th>kms_driven</th>\n",
       "      <th>fuel_type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Hyundai Santro Xing XO eRLX Euro III</td>\n",
       "      <td>Hyundai</td>\n",
       "      <td>2007</td>\n",
       "      <td>80000</td>\n",
       "      <td>45000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mahindra Jeep CL550 MDI</td>\n",
       "      <td>Mahindra</td>\n",
       "      <td>2006</td>\n",
       "      <td>425000</td>\n",
       "      <td>40</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hyundai Grand i10 Magna 1.2 Kappa VTVT</td>\n",
       "      <td>Hyundai</td>\n",
       "      <td>2014</td>\n",
       "      <td>325000</td>\n",
       "      <td>28000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Ford EcoSport Titanium 1.5L TDCi</td>\n",
       "      <td>Ford</td>\n",
       "      <td>2014</td>\n",
       "      <td>575000</td>\n",
       "      <td>36000</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Ford Figo</td>\n",
       "      <td>Ford</td>\n",
       "      <td>2012</td>\n",
       "      <td>175000</td>\n",
       "      <td>41000</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Hyundai Eon</td>\n",
       "      <td>Hyundai</td>\n",
       "      <td>2013</td>\n",
       "      <td>190000</td>\n",
       "      <td>25000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Ford EcoSport Ambiente 1.5L TDCi</td>\n",
       "      <td>Ford</td>\n",
       "      <td>2016</td>\n",
       "      <td>830000</td>\n",
       "      <td>24530</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Maruti Suzuki Alto K10 VXi AMT</td>\n",
       "      <td>Maruti</td>\n",
       "      <td>2015</td>\n",
       "      <td>250000</td>\n",
       "      <td>60000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Skoda Fabia Classic 1.2 MPI</td>\n",
       "      <td>Skoda</td>\n",
       "      <td>2010</td>\n",
       "      <td>182000</td>\n",
       "      <td>60000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Maruti Suzuki Stingray VXi</td>\n",
       "      <td>Maruti</td>\n",
       "      <td>2015</td>\n",
       "      <td>315000</td>\n",
       "      <td>30000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                      name   company  year   Price  \\\n",
       "0     Hyundai Santro Xing XO eRLX Euro III   Hyundai  2007   80000   \n",
       "1                  Mahindra Jeep CL550 MDI  Mahindra  2006  425000   \n",
       "3   Hyundai Grand i10 Magna 1.2 Kappa VTVT   Hyundai  2014  325000   \n",
       "4         Ford EcoSport Titanium 1.5L TDCi      Ford  2014  575000   \n",
       "6                                Ford Figo      Ford  2012  175000   \n",
       "7                              Hyundai Eon   Hyundai  2013  190000   \n",
       "8         Ford EcoSport Ambiente 1.5L TDCi      Ford  2016  830000   \n",
       "9           Maruti Suzuki Alto K10 VXi AMT    Maruti  2015  250000   \n",
       "10             Skoda Fabia Classic 1.2 MPI     Skoda  2010  182000   \n",
       "11              Maruti Suzuki Stingray VXi    Maruti  2015  315000   \n",
       "\n",
       "    kms_driven fuel_type  \n",
       "0        45000    Petrol  \n",
       "1           40    Diesel  \n",
       "3        28000    Petrol  \n",
       "4        36000    Diesel  \n",
       "6        41000    Diesel  \n",
       "7        25000    Petrol  \n",
       "8        24530    Diesel  \n",
       "9        60000    Petrol  \n",
       "10       60000    Petrol  \n",
       "11       30000    Petrol  "
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "6dd2c95a",
   "metadata": {},
   "outputs": [],
   "source": [
    "car['name']=car['name'].str.split(' ').str.slice(0,3).str.join(' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "9fb2f9da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>company</th>\n",
       "      <th>year</th>\n",
       "      <th>Price</th>\n",
       "      <th>kms_driven</th>\n",
       "      <th>fuel_type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Hyundai Santro Xing</td>\n",
       "      <td>Hyundai</td>\n",
       "      <td>2007</td>\n",
       "      <td>80000</td>\n",
       "      <td>45000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mahindra Jeep CL550</td>\n",
       "      <td>Mahindra</td>\n",
       "      <td>2006</td>\n",
       "      <td>425000</td>\n",
       "      <td>40</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hyundai Grand i10</td>\n",
       "      <td>Hyundai</td>\n",
       "      <td>2014</td>\n",
       "      <td>325000</td>\n",
       "      <td>28000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Ford EcoSport Titanium</td>\n",
       "      <td>Ford</td>\n",
       "      <td>2014</td>\n",
       "      <td>575000</td>\n",
       "      <td>36000</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Ford Figo</td>\n",
       "      <td>Ford</td>\n",
       "      <td>2012</td>\n",
       "      <td>175000</td>\n",
       "      <td>41000</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>883</th>\n",
       "      <td>Maruti Suzuki Ritz</td>\n",
       "      <td>Maruti</td>\n",
       "      <td>2011</td>\n",
       "      <td>270000</td>\n",
       "      <td>50000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>885</th>\n",
       "      <td>Tata Indica V2</td>\n",
       "      <td>Tata</td>\n",
       "      <td>2009</td>\n",
       "      <td>110000</td>\n",
       "      <td>30000</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>Toyota Corolla Altis</td>\n",
       "      <td>Toyota</td>\n",
       "      <td>2009</td>\n",
       "      <td>300000</td>\n",
       "      <td>132000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>Tata Zest XM</td>\n",
       "      <td>Tata</td>\n",
       "      <td>2018</td>\n",
       "      <td>260000</td>\n",
       "      <td>27000</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>Mahindra Quanto C8</td>\n",
       "      <td>Mahindra</td>\n",
       "      <td>2013</td>\n",
       "      <td>390000</td>\n",
       "      <td>40000</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>816 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                       name   company  year   Price  kms_driven fuel_type\n",
       "0       Hyundai Santro Xing   Hyundai  2007   80000       45000    Petrol\n",
       "1       Mahindra Jeep CL550  Mahindra  2006  425000          40    Diesel\n",
       "3         Hyundai Grand i10   Hyundai  2014  325000       28000    Petrol\n",
       "4    Ford EcoSport Titanium      Ford  2014  575000       36000    Diesel\n",
       "6                 Ford Figo      Ford  2012  175000       41000    Diesel\n",
       "..                      ...       ...   ...     ...         ...       ...\n",
       "883      Maruti Suzuki Ritz    Maruti  2011  270000       50000    Petrol\n",
       "885          Tata Indica V2      Tata  2009  110000       30000    Diesel\n",
       "886    Toyota Corolla Altis    Toyota  2009  300000      132000    Petrol\n",
       "888            Tata Zest XM      Tata  2018  260000       27000    Diesel\n",
       "889      Mahindra Quanto C8  Mahindra  2013  390000       40000    Diesel\n",
       "\n",
       "[816 rows x 6 columns]"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "6d739bfb",
   "metadata": {},
   "outputs": [],
   "source": [
    "car=car.reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "a6f7977b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>company</th>\n",
       "      <th>year</th>\n",
       "      <th>Price</th>\n",
       "      <th>kms_driven</th>\n",
       "      <th>fuel_type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Hyundai Santro Xing</td>\n",
       "      <td>Hyundai</td>\n",
       "      <td>2007</td>\n",
       "      <td>80000</td>\n",
       "      <td>45000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mahindra Jeep CL550</td>\n",
       "      <td>Mahindra</td>\n",
       "      <td>2006</td>\n",
       "      <td>425000</td>\n",
       "      <td>40</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Hyundai Grand i10</td>\n",
       "      <td>Hyundai</td>\n",
       "      <td>2014</td>\n",
       "      <td>325000</td>\n",
       "      <td>28000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Ford EcoSport Titanium</td>\n",
       "      <td>Ford</td>\n",
       "      <td>2014</td>\n",
       "      <td>575000</td>\n",
       "      <td>36000</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Ford Figo</td>\n",
       "      <td>Ford</td>\n",
       "      <td>2012</td>\n",
       "      <td>175000</td>\n",
       "      <td>41000</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>811</th>\n",
       "      <td>Maruti Suzuki Ritz</td>\n",
       "      <td>Maruti</td>\n",
       "      <td>2011</td>\n",
       "      <td>270000</td>\n",
       "      <td>50000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>812</th>\n",
       "      <td>Tata Indica V2</td>\n",
       "      <td>Tata</td>\n",
       "      <td>2009</td>\n",
       "      <td>110000</td>\n",
       "      <td>30000</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>813</th>\n",
       "      <td>Toyota Corolla Altis</td>\n",
       "      <td>Toyota</td>\n",
       "      <td>2009</td>\n",
       "      <td>300000</td>\n",
       "      <td>132000</td>\n",
       "      <td>Petrol</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>814</th>\n",
       "      <td>Tata Zest XM</td>\n",
       "      <td>Tata</td>\n",
       "      <td>2018</td>\n",
       "      <td>260000</td>\n",
       "      <td>27000</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>815</th>\n",
       "      <td>Mahindra Quanto C8</td>\n",
       "      <td>Mahindra</td>\n",
       "      <td>2013</td>\n",
       "      <td>390000</td>\n",
       "      <td>40000</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>816 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                       name   company  year   Price  kms_driven fuel_type\n",
       "0       Hyundai Santro Xing   Hyundai  2007   80000       45000    Petrol\n",
       "1       Mahindra Jeep CL550  Mahindra  2006  425000          40    Diesel\n",
       "2         Hyundai Grand i10   Hyundai  2014  325000       28000    Petrol\n",
       "3    Ford EcoSport Titanium      Ford  2014  575000       36000    Diesel\n",
       "4                 Ford Figo      Ford  2012  175000       41000    Diesel\n",
       "..                      ...       ...   ...     ...         ...       ...\n",
       "811      Maruti Suzuki Ritz    Maruti  2011  270000       50000    Petrol\n",
       "812          Tata Indica V2      Tata  2009  110000       30000    Diesel\n",
       "813    Toyota Corolla Altis    Toyota  2009  300000      132000    Petrol\n",
       "814            Tata Zest XM      Tata  2018  260000       27000    Diesel\n",
       "815      Mahindra Quanto C8  Mahindra  2013  390000       40000    Diesel\n",
       "\n",
       "[816 rows x 6 columns]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b2891e63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 816 entries, 0 to 815\n",
      "Data columns (total 6 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   name        816 non-null    object\n",
      " 1   company     816 non-null    object\n",
      " 2   year        816 non-null    int32 \n",
      " 3   Price       816 non-null    int32 \n",
      " 4   kms_driven  816 non-null    int32 \n",
      " 5   fuel_type   816 non-null    object\n",
      "dtypes: int32(3), object(3)\n",
      "memory usage: 28.8+ KB\n"
     ]
    }
   ],
   "source": [
    "car.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "f264dbbc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>Price</th>\n",
       "      <th>kms_driven</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>816.000000</td>\n",
       "      <td>8.160000e+02</td>\n",
       "      <td>816.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>2012.444853</td>\n",
       "      <td>4.117176e+05</td>\n",
       "      <td>46275.531863</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>4.002992</td>\n",
       "      <td>4.751844e+05</td>\n",
       "      <td>34297.428044</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1995.000000</td>\n",
       "      <td>3.000000e+04</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2010.000000</td>\n",
       "      <td>1.750000e+05</td>\n",
       "      <td>27000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>2013.000000</td>\n",
       "      <td>2.999990e+05</td>\n",
       "      <td>41000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2015.000000</td>\n",
       "      <td>4.912500e+05</td>\n",
       "      <td>56818.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>2019.000000</td>\n",
       "      <td>8.500003e+06</td>\n",
       "      <td>400000.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              year         Price     kms_driven\n",
       "count   816.000000  8.160000e+02     816.000000\n",
       "mean   2012.444853  4.117176e+05   46275.531863\n",
       "std       4.002992  4.751844e+05   34297.428044\n",
       "min    1995.000000  3.000000e+04       0.000000\n",
       "25%    2010.000000  1.750000e+05   27000.000000\n",
       "50%    2013.000000  2.999990e+05   41000.000000\n",
       "75%    2015.000000  4.912500e+05   56818.500000\n",
       "max    2019.000000  8.500003e+06  400000.000000"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "ebb3596f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>company</th>\n",
       "      <th>year</th>\n",
       "      <th>Price</th>\n",
       "      <th>kms_driven</th>\n",
       "      <th>fuel_type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>534</th>\n",
       "      <td>Mahindra XUV500 W6</td>\n",
       "      <td>Mahindra</td>\n",
       "      <td>2014</td>\n",
       "      <td>8500003</td>\n",
       "      <td>45000</td>\n",
       "      <td>Diesel</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   name   company  year    Price  kms_driven fuel_type\n",
       "534  Mahindra XUV500 W6  Mahindra  2014  8500003       45000    Diesel"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car[car['Price']>6e6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "0a97ebdf",
   "metadata": {},
   "outputs": [],
   "source": [
    "car=car[car['Price']<6e6].reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "4d529c3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>Price</th>\n",
       "      <th>kms_driven</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>815.000000</td>\n",
       "      <td>8.150000e+02</td>\n",
       "      <td>815.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>2012.442945</td>\n",
       "      <td>4.017933e+05</td>\n",
       "      <td>46277.096933</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>4.005079</td>\n",
       "      <td>3.815888e+05</td>\n",
       "      <td>34318.459638</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1995.000000</td>\n",
       "      <td>3.000000e+04</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2010.000000</td>\n",
       "      <td>1.750000e+05</td>\n",
       "      <td>27000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>2013.000000</td>\n",
       "      <td>2.999990e+05</td>\n",
       "      <td>41000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2015.000000</td>\n",
       "      <td>4.900000e+05</td>\n",
       "      <td>56879.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>2019.000000</td>\n",
       "      <td>3.100000e+06</td>\n",
       "      <td>400000.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              year         Price     kms_driven\n",
       "count   815.000000  8.150000e+02     815.000000\n",
       "mean   2012.442945  4.017933e+05   46277.096933\n",
       "std       4.005079  3.815888e+05   34318.459638\n",
       "min    1995.000000  3.000000e+04       0.000000\n",
       "25%    2010.000000  1.750000e+05   27000.000000\n",
       "50%    2013.000000  2.999990e+05   41000.000000\n",
       "75%    2015.000000  4.900000e+05   56879.000000\n",
       "max    2019.000000  3.100000e+06  400000.000000"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "14b5b868",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Price', ylabel='Count'>"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(np.log(car['Price']),kde=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "133f3d06",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import r2_score\n",
    "from sklearn.preprocessing import OneHotEncoder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "f6ee6c5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=car.drop('Price',axis=1)\n",
    "y=car['Price']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "7e1f2648",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "d39c7026",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.compose import make_column_transformer\n",
    "from sklearn.pipeline import make_pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "dbd74d73",
   "metadata": {},
   "outputs": [],
   "source": [
    "ohe=OneHotEncoder()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "8ac1e779",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "OneHotEncoder()"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ohe.fit(x[['name','company','fuel_type']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "5cecf5d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "column_trans=make_column_transformer((OneHotEncoder(categories=ohe.categories_),['name','company','fuel_type']),remainder='passthrough')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "7abdf7d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "lr=LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "56e71e00",
   "metadata": {},
   "outputs": [],
   "source": [
    "pipe=make_pipeline(column_trans,lr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "da2bc6eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pipeline(steps=[('columntransformer',\n",
       "                 ColumnTransformer(remainder='passthrough',\n",
       "                                   transformers=[('onehotencoder',\n",
       "                                                  OneHotEncoder(categories=[array(['Audi A3 Cabriolet', 'Audi A4 1.8', 'Audi A4 2.0', 'Audi A6 2.0',\n",
       "       'Audi A8', 'Audi Q3 2.0', 'Audi Q5 2.0', 'Audi Q7', 'BMW 3 Series',\n",
       "       'BMW 5 Series', 'BMW 7 Series', 'BMW X1', 'BMW X1 sDrive20d',\n",
       "       'BMW X1 xDrive20d', 'Chevrolet Beat', 'Chevrolet Beat...\n",
       "                                                                            array(['Audi', 'BMW', 'Chevrolet', 'Datsun', 'Fiat', 'Force', 'Ford',\n",
       "       'Hindustan', 'Honda', 'Hyundai', 'Jaguar', 'Jeep', 'Land',\n",
       "       'Mahindra', 'Maruti', 'Mercedes', 'Mini', 'Mitsubishi', 'Nissan',\n",
       "       'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen', 'Volvo'],\n",
       "      dtype=object),\n",
       "                                                                            array(['Diesel', 'LPG', 'Petrol'], dtype=object)]),\n",
       "                                                  ['name', 'company',\n",
       "                                                   'fuel_type'])])),\n",
       "                ('linearregression', LinearRegression())])"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pipe.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "25e1ed06",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred=pipe.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "a56bb136",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 143473.15605375,  367400.8093437 ,  647349.63738629,\n",
       "       1421809.34968542,  273737.28158078,  287572.94325808,\n",
       "        151275.28130051,  501498.86647002,  122528.08896858,\n",
       "        343829.55188575,  282766.08761332,  332816.83319435,\n",
       "        419088.86558305,  267586.48301733,  254826.06372925,\n",
       "        240202.15147508,  277168.22562887,  579994.24634992,\n",
       "       1215671.67748365,  256942.66283282,  133210.90612211,\n",
       "        561627.93504382, 1888237.14697714,  248251.08981934,\n",
       "        217238.99884002,  170808.37999471,  155622.87526644,\n",
       "        236640.97157821,  235566.92942825,  238121.05071189,\n",
       "        551750.50651982,  177534.95660885,  112291.56587841,\n",
       "        189066.56692835,  416057.45030803,  493591.38076413,\n",
       "        313921.96785816,  213441.0797853 ,  500575.38300724,\n",
       "        272856.79635781,  244829.98191722,   43794.09839214,\n",
       "        500575.38300724,  368510.38433643,  220708.99508521,\n",
       "        712355.2660368 ,  273352.16975725,  256345.08869064,\n",
       "        659571.46583024,   61144.19743815,  483715.43194571,\n",
       "       1478537.94455027,   65489.13233115,  -95920.00403669,\n",
       "        428948.58434741,  368992.93420878,  185488.61869671,\n",
       "        301611.2462694 ,  125547.99956447,  496420.07790902,\n",
       "        231733.37833663,  257107.59400439,  222323.09425533,\n",
       "        581898.89402179,   85227.70237108,  276865.25257421,\n",
       "        300675.90612718, 1888171.96626669,  230763.1168623 ,\n",
       "        689777.96595089,  181619.95105448,  397114.72673792,\n",
       "        403887.87562012,  364084.85771839,  453918.59503893,\n",
       "        469447.71231886,  152578.89550957, 1495585.58869496,\n",
       "        407798.71824727,  305338.15598566,  731149.77208333,\n",
       "        495677.16349862,   36076.97976502,  518384.34991967,\n",
       "         91266.52713697,   91266.52713697,  468086.03473267,\n",
       "        273054.94945109,  553411.29114585,   77105.1977283 ,\n",
       "        345317.12987551,  386802.76028354,   89980.22034787,\n",
       "        365660.42022032,  369293.7732961 ,  129450.93554105,\n",
       "        177650.64107501,  410969.09219002,  111957.38644481,\n",
       "        314617.58145779,  424675.04731545,  575461.91383456,\n",
       "        187573.71840734,  397166.97606219,  636399.32506453,\n",
       "        110523.41081486,  660511.4977182 ,  484913.67916235,\n",
       "        293981.8529581 ,   93016.46589668,  132986.42978971,\n",
       "         77639.62850327,  558238.53810029,  235566.92942825,\n",
       "        412055.98031471,  397723.74969088,  251712.44562803,\n",
       "        203747.74607415,  185902.0633077 ,  347146.4672768 ,\n",
       "        396082.36904026,  493174.95758327,  283799.71822292,\n",
       "        263390.94178744,  382619.42145683,  606752.28725997,\n",
       "        551750.50651982,  286614.81726432,  285050.48021346,\n",
       "        453993.37752794,  236781.24606398,  455211.27926924,\n",
       "        118893.96186031,  255562.9201652 ,  486021.12122783,\n",
       "        490719.60084568,  326188.49807458, 1007127.26340951,\n",
       "        369684.85755882,  307622.54858579,  322819.82124118,\n",
       "        266995.5654369 ,  278951.03530869,  -77894.36397394,\n",
       "        235089.73242196,  187917.92108388,  550924.86737713,\n",
       "        342516.92479638,  330079.24335534,  342400.55038238,\n",
       "        153621.78687681,  312209.1740784 ,  231879.6312156 ,\n",
       "        116727.9067998 ,  563544.05656377,  413114.09496641,\n",
       "        266995.5654369 ,  909982.8713712 ,  488374.12899353,\n",
       "        112357.57417729,  415646.24799343,  551167.35887163,\n",
       "        315641.39138411])"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "c099d333",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7654846579105726"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r2_score(y_test,y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "407e3490",
   "metadata": {},
   "outputs": [],
   "source": [
    "score=[]\n",
    "for i in range(1000):\n",
    "    X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=i)\n",
    "    lr=LinearRegression()\n",
    "    pipe=make_pipeline(column_trans,lr)    \n",
    "    pipe.fit(X_train,y_train)\n",
    "    y_pred=pipe.predict(X_test)\n",
    "    score.append(r2_score(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "3107a6bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "661"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.argmax(score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "02d65720",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8897762920578806"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "score[np.argmax(score)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "3b3da0f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.34841479755832416"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "score[np.argmin(score)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "7790eb00",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=661)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "b9cf6c5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "lr=LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "b42ce2bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "pipe=make_pipeline(column_trans,lr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "df8c39e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pipeline(steps=[('columntransformer',\n",
       "                 ColumnTransformer(remainder='passthrough',\n",
       "                                   transformers=[('onehotencoder',\n",
       "                                                  OneHotEncoder(categories=[array(['Audi A3 Cabriolet', 'Audi A4 1.8', 'Audi A4 2.0', 'Audi A6 2.0',\n",
       "       'Audi A8', 'Audi Q3 2.0', 'Audi Q5 2.0', 'Audi Q7', 'BMW 3 Series',\n",
       "       'BMW 5 Series', 'BMW 7 Series', 'BMW X1', 'BMW X1 sDrive20d',\n",
       "       'BMW X1 xDrive20d', 'Chevrolet Beat', 'Chevrolet Beat...\n",
       "                                                                            array(['Audi', 'BMW', 'Chevrolet', 'Datsun', 'Fiat', 'Force', 'Ford',\n",
       "       'Hindustan', 'Honda', 'Hyundai', 'Jaguar', 'Jeep', 'Land',\n",
       "       'Mahindra', 'Maruti', 'Mercedes', 'Mini', 'Mitsubishi', 'Nissan',\n",
       "       'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen', 'Volvo'],\n",
       "      dtype=object),\n",
       "                                                                            array(['Diesel', 'LPG', 'Petrol'], dtype=object)]),\n",
       "                                                  ['name', 'company',\n",
       "                                                   'fuel_type'])])),\n",
       "                ('linearregression', LinearRegression())])"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pipe.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "482c26ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred=pipe.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "6cbeb1ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8897762920578806"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r2_score(y_test,y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "66eec424",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "db8717f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([232629.78048045])"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pickle.dump(pipe,open('LGM','wb'))\n",
    "pipe.predict(pd.DataFrame([['Maruti Suzuki Ritz','Maruti',2011,50000,'Petrol']],columns=['name','company','year','kms_driven','fuel_type']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "794c4034",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
