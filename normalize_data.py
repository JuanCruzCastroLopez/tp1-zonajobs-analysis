import pandas as pd

def getNormalizedDataset():    # write Fibonacci series up to n
  df = pd.read_csv('train.csv',
          index_col='id',
          dtype={'gimnasio': bool,
                'usosmultiples': bool,
                'escuelascercanas': bool,
                'piscina': bool,
                'centroscomercialescercanos': bool,
                'tipodepropiedad': 'category',
                'provincia': 'category',
                'ciudad': 'category'
                }
          parse_dates=['fecha'])

  return df

