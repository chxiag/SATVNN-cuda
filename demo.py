from dataHelpers import generate_data
import numpy as np
import matplotlib.pyplot as plt
from SATVNN import SATVNN
from evaluate import evaluate
from train import train

#Use a fixed seed for repreducible results
np.random.seed(1)

# Generate the dataset Pphil
data = np.array([76.2,  64.8, 127.3,  76.2, 166.6, 47.8, 165.1,  92.5,  49.5, 227.1,  79.2,  82.6,
  12.2, 122.4,  14.5,  77.5, 150.4,  66.0,  46.7,  10.4, 145.8,  82.3, 118.1,  72.1,
  43.2, 73.7,  55.9,   54.9,  55.1,  36.6,  96.5,  33.8, 138.4,  31.5, 127.0,  31.8,
  85.9,  98.0, 174.5,  45.0,  40.6,  22.1, 155.4, 118.9,  87.9,  51.3,  62.7, 187.2,
  93.2, 100.1,  66.8,  115.3,  40.4, 154.7, 223.5, 162.3, 154.9,  38.9,  63.2,  53.6,
  21.3,  82.8, 117.6,  21.1,  43.7,  93.7,  52.3,  94.0,  66.3,  31.8,  34.5,  94.5,
  28.2,  54.1, 147.3,  98.3,   4.8, 118.4,  93.5,  69.9,  50.8, 148.1,  47.0,  32.5,
  72.6,  90.2,  31.2,  71.9,  63.5,  53.1, 75.4, 146.1,  20.1, 150.1, 120.9,  82.8,
  52.1,  69.9,  85.1,  97.0,  88.6,  68.3, 135.4,  38.4, 117.3,  35.3, 170.4,   6.6,
 136.4,  95.3,  72.9, 126.7,  68.1,  87.4, 110.5, 117.1,  51.1,  58.4, 100.8,  38.4,
  41.4,  52.3, 104.6,  46.2,  95.3, 152.1, 103.4,  98.3,  74.4, 109.5, 135.9, 131.6,
 158.0,  62.0,  75.4, 132.1,  27.2,  90.4, 105.9, 136.9, 135.4, 114.6,  47.8,  30.5,
 116.3,  67.6,  48.3, 75.7, 128.0,  39.4,  66.5, 144.5,  35.6,  86.6,  65.8, 129.3,
 100.8,  31.5,  56.4,  17.8, 149.4, 134.1, 105.4,  86.1,  97.0, 255.3,  55.4, 144.0,
  63.2,  56.4,  51.3,  71.9,  89.4, 101.3, 110.5,  15.7,  90.7,  83.6,  76.5,  59.2,
  69.9,  46.0,  97.3, 110.0,  50.5, 159.3, 166.4,  52.1,  66.8,  31.0,  81.0,  68.1,
 193.5,  75.9,  44.5,  88.1,  57.9, 185.7,  73.9,  50.0,  46.2,  91.2,  84.8,  91.7,
  63.5,  90.9,  95.5,  71.9, 123.4,  71.9, 149.6, 103.1,  57.9,  16.8,  82.0,  65.0,
  55.9,  55.6,  80.5,  91.2,  90.9, 167.6,  60.5,  70.6, 241.8, 124.5,  85.1,  26.7,
 128.0,  86.9,  38.4,  38.4, 154.2,  99.6,  64.0, 117.9,  74.2,  71.9,  78.7, 159.0,
  46.7,  76.5,  66.8, 173.5,  68.3, 151.1, 115.3, 141.0,  63.5, 145.5,  63.2,  92.7,
 199.1,  35.3, 147.8, 163.8,  83.1,  79.0,  83.3, 231.1,  48.3,  81.3, 107.2, 150.4,
  34.5, 108.2,  72.1, 134.9, 148.8,  81.0, 299.7,  96.3,  32.3,  43.4,  88.6,  93.0,
  36.6,  64.5, 112.3, 119.9,  52.1,  42.9, 115.3, 235.2, 123.4,  81.8, 105.4, 102.6,
 102.9,  36.8, 112.5,  34.3,  78.5,  85.1, 134.1,  61.0, 102.4, 127.8,  74.9, 69.9,
  95.5, 120.4,  61.5,  65.5,  40.6,  94.5,  75.2, 185.4,  54.9,  64.3,  63.5, 100.6,
 117.6,  84.6, 116.8,  53.6,  87.6,  83.8, 116.8, 108.5,   6.4,  62.2, 202.4,  87.4,
 120.1, 116.1, 119.4,  15.0,  39.9,  84.1,  70.1,  80.8, 205.0,  76.2,  72.1, 147.1,
  51.6,  36.6,  69.9,  39.1, 124.5, 112.5,  83.3,  43.7,  46.0,  95.3,  59.4, 127.3,
  18.5,  66.3, 138.9,  44.5, 101.6,  55.9,  74.4, 177.0,  35.8, 142.2,  66.0, 148.3,
 121.2,  72.9, 120.7,  67.8, 165.1,  51.6, 151.6, 211.6, 196.3,  27.7,  84.3, 114.8,
  31.2,  79.0,  88.1, 115.8, 122.4,  87.4,  64.0,  65.0,  28.7,  77.0,  85.1,  57.9,
  51.1,  68.8, 108.5, 163.8,  77.0, 102.4, 103.1, 111.8,  32.8,  57.7, 153.9, 131.3,
  47.0, 112.8,  62.5,  97.5, 131.3,  27.9, 160.0,  78.5, 113.3,  88.1,  58.9,  55.1,
  59.2, 106.9,  41.1, 196.9, 176.3,  60.7,  76.7,  21.3,  96.5,  39.4,  71.9,  73.9,
  59.4,  59.7,  42.7,  52.1,  75.2, 201.9, 162.6,  70.9, 101.6, 104.4,  51.8, 137.9,
 115.3,  31.5,  56.6,  89.4,  66.0,  50.5,  38.4, 152.4, 101.9,  33.0,  52.6,  74.7,
  89.7,  20.1,  46.5, 172.2, 141.0, 190.5,  99.6, 192.8,  28.2,  68.3,  36.8, 141.0,
  65.8, 58.2,  27.7, 117.9 ,127.5,  114.0,  34.3, 125.5,  37.8,  46.7, 142.5,114.3,
 169.7,  93.0, 177.3, 142.5,  57.2, 152.7, 103.4, 120.1, 195.1,  79.5,  97.0,  88.6,
  82.0,  70.1,  36.1,  96.5,  97.0,  73.2,  25.1, 214.9,  72.4, 114.8, 155.7,  84.1,
 133.4,  52.6,  99.6,  94.2, 168.7,  98.6,  65.0,  79.8, 111.8,  96.5, 123.7,  53.1,
 121.7, 117.9,  90.2, 105.7,  58.7, 177.0,  62.7,  23.6, 101.1, 121.2, 121.7,  41.9,
 119.9, 118.9, 149.6,178.3, 114.6, 108.0 ,152.7,  36.8,  22.4 , 62.5,  68.6 ,117.6,
  43.4,  14.0, 131.3,  96.5, 220.5,  59.7,  95.8,  48.8, 181.9,  46.2,  99.8, 130.8,
  91.7, 148.1, 119.6,  71.9, 183.1, 120.7,  75.4,  95.8, 202.2,  77.5, 100.6, 142.5,
  80.0, 167.9,  54.6,  74.4, 118.9,  75.2,  64.0,  55.4, 221.2, 105.4,  44.7,  88.1,
  44.7,  98.8, 138.9,  46.0, 185.9, 280.2,  60.7, 401.8,  43.7, 109.7,  74.7,  69.3,
  91.9,  64.0, 85.3, 138.2, 178.1, 111.0,  89.2,  52.3, 226.3,  44.2, 134.1,  91.4,
 108.7, 120.9, 134.9,  53.8, 107.7, 141.7,  73.4,  32.5,  82.6, 160.5,  94.7, 130.0,
 103.6,  64.3, 103.1, 142.5, 159.5,  73.7, 100.3, 130.0,  43.4,  98.8,  53.3,  48.0,
  88.1,  78.5, 147.6,  46.5,  85.9,  96.0, 173.0, 151.6,  45.0, 123.4, 109.0,  57.4,
  37.8,  28.4,  93.2, 66.0,  80.0, 109.0, 233.7, 198.4,  93.0, 132.1,  87.1,  69.6,
 148.3, 120.7,  52.1,  89.2, 148.1,  22.9, 127.0, 291.8,  92.2, 147.3, 129.5,  35.1,
 116.3,  62.5,  54.9, 247.9,  69.9,  75.2,  57.2, 143.5, 152.7,  72.9,  58.9,  63.0,
  71.9,  81.3,  78.7,  71.9,  34.5, 104.9,  92.2, 163.1,  64.3,  36.1, 137.2,  85.6,
  38.6, 127.8, 170.4,  54.9, 113.0,  58.2, 145.0,  24.9, 222.8,  26.9, 185.7,  35.6,
  66.5,  21.3,  86.4,  67.6,  27.9, 132.6, 140.5,  16.8,  69.6, 165.6, 130.6,  21.1,
 100.1,  41.7,  73.4,  64.8,  83.6,  93.0, 110.5,  97.3,  24.4,  51.8,  55.6,  81.0,
  69.3,  30.2,  57.9, 106.9,  31.0, 172.0,  92.2, 181.1,  28.4,  10.4,  35.1, 119.1,
  38.4,  61.7,  89.7, 61.7 , 13.7,  42.4 ,196.6, 129.3,  27.9,  44.2,  44.5, 102.9,
  93.0, 120.9,  97.3,  15.5,  68.8,  98.3,  24.4,  30.0,  23.9,  77.2,  51.3,  66.8,
 116.1, 107.2,  90.7,  53.8, 128.5,  48.3,  34.8, 162.6, 307.1,  33.5,  25.1,  50.0,
 104.9, 128.0,  51.3,  62.0,  48.5, 150.1,  45.2,  86.4, 107.7, 106.7,  34.0,  70.1,
 138.7, 144.8, 119.4,  41.4,  86.1,  76.2,  97.3, 109.2,   5.1,  39.1,  58.7,  83.3,
  74.2,  70.9,  17.5,  64.5,  95.5,  18.8,  60.7, 172.7,  29.7,  84.6,  85.1,  72.9,
  93.7, 117.3,  80.5,  68.6, 114.3,  72.6, 107.4,  35.1,  30.5,  48.0,  99.3,  78.5,
  82.0, 112.5,  65.8,  50.8,  15.7, 173.0, 181.4,  58.7, 125.0,  42.7,  35.1, 128.5,
 109.2,  65.3, 137.7,  53.3,  87.9,  27.7,  85.9, 148.8, 145.5,  82.0,  95.8,  80.0,
  95.3,  50.8,  65.5,  80.5, 109.7,  86.1, 210.6, 179.6, 118.4,  95.5, 171.7,  21.6,
  46.5,  86.1, 117.1,  57.9,  75.2,  33.0, 102.4,  85.3,  58.7, 122.4,  20.3,  59.2,
  92.7, 119.6, 112.3,  59.4,  44.2,  63.8, 118.1, 107.2,  48.3,  65.3,  43.2,  96.0,
 113.8,  24.9, 109.7,  51.6, 130.0,  50.3,  75.4,  69.6,  52.3,   7.6, 145.0,  53.1,
  65.5, 123.2,  65.3, 113.5,  74.2,  78.0,  51.8,  61.7,  95.5,  84.3,  63.8,  79.5,
  45.2,  78.0,  36.8,  75.9, 240.3,  41.4,  19.1,  54.6, 129.8, 118.4,  82.8, 102.4,
 114.8,  35.3,  66.3, 156.0,  43.7,  80.0,  82.0,  15.0,  15.5,  75.4,  58.9,  44.7,
  39.9, 174.5, 104.4,  30.2,  57.7, 103.4,  83.1,  11.7,  70.1,  52.8,  63.5,  25.4,
  55.1,  75.4,  51.6,  77.0, 110.0, 115.1, 195.6,  89.4,  27.9,  43.2, 112.8, 114.8,
 104.1,  71.1,  77.5,  74.4, 122.9,  44.5,  92.2, 230.1,  46.2, 123.2, 182.6,  81.5,
 101.9, 157.5, 164.3,  26.4,  58.4,  27.7, 119.1, 131.6,  93.0,  50.3,  49.0,  35.8,
  84.8,  94.2,  79.5,  49.3, 104.4,  71.6,  70.4, 100.3, 160.3,  76.2,  86.9,  61.2,
  62.7,  21.8,  86.1, 121.2, 102.9,  29.2, 124.0, 239.3,  93.5,  38.4,  67.1, 170.7,
  70.4, 139.4, 100.8,  83.6,  51.1, 154.4,  89.2,  59.4, 126.2, 169.2,  51.8, 168.4,
  89.4, 109.0, 111.3,  76.2,  23.6, 139.2,  97.5, 141.5,  58.7,  98.0,  26.2,  83.6,
  79.8,  56.1,  82.3,  48.0,  52.8,  73.2,  97.0, 112.5, 183.1, 102.4,  64.8,  57.9,
  79.2,  65.0, 106.2,  90.9,  35.8,  45.0,  79.0, 243.1,  92.7, 103.4,  40.9,  75.7,
  80.3,  62.7, 142.0,  80.5, 112.5, 204.2, 135.4, 242.8,   9.1, 126.2,  43.7,  78.0,
  67.3,  69.9,  71.4,  73.2, 142.5, 118.4,  99.1,  91.2, 152.1,  85.9, 148.6 ,118.6,
  79.8,  81.5,  71.9,  59.7, 174.0,  61.2, 115.3, 137.4,  45.5,  46.0,  17.0,  79.2,
  64.0, 117.3,  74.2,114.0,  67.8,  57.4,  55.6 , 49.5,  90.2,  21.1,  88.9, 148.8,
 107.4,  75.9,   9.7, 120.9,  54.1, 137.2,  46.7, 145.3,  77.5,  73.7,  92.7,  64.8,
  81.8,  68.3,  69.1,  93.5,  42.7, 129.5, 106.4, 307.3,  64.0, 106.7, 141.7,  93.2,
  65.3,  83.8, 231.1,  73.4, 136.7,  48.5, 105.4,  43.4, 142.7,  61.5,  81.5, 120.4,
  75.9,  48.3, 118.4, 174.5, 117.6,  54.6, 109.0, 117.1, 107.7, 143.8,  72.4,  65.0,
  87.9,  84.3,  68.8,  87.1,  22.9,  94.0, 196.9,  58.7,  21.8,  37.8,  45.5, 186.7,
 171.2, 141.0,  25.4, 107.4, 104.6,  87.6, 127.5, 173.7,  11.7,  50.3,  31.0, 107.2,
  38.1,  90.2,  95.3,  75.4,  69.9,  71.9,  86.4 , 23.9,  62.0,  30.7,  37.6, 138.4,
  48.3,  55.9, 138.7,  62.7,  75.2,  57.2, 143.0 , 97.0,  83.1, 153.4,  21.8,  64.3,
 103.1,  39.9,  58.4, 112.3, 173.0,  54.6,  62.5,  85.1,  95.5,  17.5,  49.0, 107.4,
  85.1,  77.2, 122.2,  80.5, 115.1,  55.6, 261.6, 157.2,  71.6,  65.8,  71.1,  84.6,
  68.8,  93.2,  85.1,  99.6 , 54.6, 171.7,  89.4, 185.7,  86.9,  16.3, 102.9, 118.4,
  51.6, 111.8,  62.0,  47.0,  86.9,  72.6, 102.6, 152.7,  56.1,  10.2,  93.7,  53.3,
  80.3,  66.5, 110.2,  38.6,  62.7, 115.8,  61.5,  65.0,  31.2,  18.0,  10.9 , 83.6,
 121.4,  68.8,  90.9, 129.3,  31.2,  16.5,  89.2, 108.2,  92.5,  95.8,  48.5, 103.1,
 113.0, 116.1,  87.6, 136.4, 124.7, 109.5,  80.8,  95.8, 129.0,   2.3,  44.5,  55.4,
 118.9,  42.2,  80.0,  61.7,  59.9,  29.5, 126.7,  51.1,  48.0, 105.2,  75.4,  24.4,
  72.4,  80.8,  49.8,  46.0,  58.7,  71.4, 213.4, 152.1, 124.0, 104.4,  78.0,  89.9,
  47.8,  91.9,  28.2,  93.0,  44.5,  88.4, 114.3, 184.7,  65.8, 145.0,  91.2, 101.3,
  48.5, 101.6,  53.3, 141.0,  55.6, 172.0,  91.4, 137.4,  91.7,  18.5,  49.3,  38.1,
  68.6, 107.7,  56.4, 163.6 , 57.9,  69.6,  38.9,  81.8, 165.4,  91.2,  79.0,  75.7,
  80.0,  92.7,  65.5,  41.7,  82.6, 126.0,  103.1,  38.4,  65.3,  44.2,  59.9,  63.5,
  55.1,  48.8, 100.8,  52.1 ,112.8,  95.3, 202.9, 152.4,  40.6,  66.3,  25.4 , 45.2,
 119.1,  40.1, 188.7,  60.2 , 96.8,  86.1,  57.2,  78.0,  26.7, 109.2, 189.2 , 79.5,
  67.6,  81.0, 123.4, 133.6, 176.0, 121.4, 119.4, 249.9, 105.9,  35.3,  27.2,  64.0,
  73.9,  69.9,  74.2,  79.0 , 99.6,  81.8,  55.4, 109.0, 159.3,  39.1,  67.1,  66.3,
 106.9,  79.2,  53.6,  53.8 , 56.1, 158.8, 128.8,  84.8, 212.3, 100.3, 103.4,  39.4,
 163.6,  87.9, 102.1,  57.2,  42.4, 100.6,  66.0,  83.8,  94.5,  44.7,  17.5, 122.7,
 145.0,  42.2,  75.7, 111.3,  66.5,  89.2,  29.5, 104.1,  39.4, 133.1,  87.4,  26.7,
  58.9,  64.5,  46.5,  48.8,  72.6, 255.5, 165.6, 104.1, 186.7,  53.1,  79.0,  56.4,
 113.3, 155.4, 109.7, 162.6 , 48.5, 113.0,  55.6, 175.3,  48.5, 109.2,  32.0,  30.0,
  24.4,  73.7, 104.1, 153.9, 124.2,  64.0,  46.2, 199.9, 116.3,  60.5, 107.7,  64.3,
  80.3,  52.8,  71.1,  63.0,  22.1, 126.0, 142.2,  65.8,  13.0,  27.9,  59.9,  93.2,
  59.4,  58.4, 122.9,  34.3,  46.2,  54.1, 171.2, 166.4,  42.7,  86.4,  96.3, 107.2,
  86.6,  42.7,  79.2,  52.1, 152.4,  80.8, 108.2,  15.7,  30.0, 132.1,  71.1,  31.0,
  74.7,  50.5, 150.1, 125.2,  50.0,  53.3,  18.5,  62.0, 154.4,  41.7, 109.5,  85.3,
  69.3,  80.0,  40.9,  74.9,  84.6,101.1, 225.0,  95.3, 100.6 , 48.3, 144.5, 128.3,
  38.4,  52.3,  68.6,  37.1, 148.6, 218.7, 131.6, 112.8,  81.8,  31.0,  47.5,  70.1,
  96.8,  61.5,  55.6, 171.7, 220.5, 119.4,  63.2, 181.6,  73.9,  64.8, 166.9,  48.0,
 137.7,  80.5, 105.2,  89.9, 174.8, 124.0,  86.4, 136.9,  31.5,  35.3, 112.3, 143.0,
 160.8,  97.0,  80.5,  62.5, 158.2,   7.6, 165.9, 106.7,  92.2,  63.2,  26.2,  77.0,
  52.3, 105.4, 144.3,  49.5, 116.1,  54.1, 148.6, 159.3,  85.3,  67.3, 112.8,  59.4])


train_x, train_y, test_x, test_y, valid_x, valid_y, period,mm = generate_data(data,period = 12)

# Model parameters
in_seq_length = 2 * period
out_seq_length = period
hidden_dim = 75
head = 1
M = 2
input_dim = 1
output_dim = 1
learning_rate = 0.001
batch_size = 16
dis_alpha = 0.1
d_model = 70

# Initialise model
SA = SATVNN(in_seq_length=in_seq_length, out_seq_length=out_seq_length, d_model=d_model,input_dim=input_dim,
                        hidden_dim=hidden_dim, h=head, M=M, output_dim=output_dim, batch_size = batch_size,
                        period=period, n_epochs = 100, learning_rate = learning_rate, train_x=train_x, save_file = './satvnn.pt')

# Train the model
training_costs, validation_costs = train(SA, train_x, train_y, valid_x, valid_y, restore_session=False)

# Plot the training curves
# plt.figure()
# plt.plot(training_costs)
# plt.plot(validation_costs)

# Evaluate the model
mase,smape, nrmse = evaluate(SA, test_x, test_y, return_lists=False)

print('MASE:', mase)
print('SMAPE:', smape)


# Generate and plot forecasts for various samples from the test dataset
samples = [0, 12, 23]
predict_start = 24
y_pred = SA.forecast(test_x[:,samples,:],predict_start)
for i in range(len(samples)):
    pred= mm.inverse_transform(y_pred[:, i, 0][:,np.newaxis])
    true = mm.inverse_transform(test_y[:, samples[i], 0][:,np.newaxis])
    plt.figure()
    plt.plot(np.arange(0, SA.in_seq_length),
             test_x[:, samples[i], 0],
             '*-', label='test_data')
    plt.plot(np.arange(SA.in_seq_length, SA.in_seq_length + SA.out_seq_length),
             test_y[:, samples[i], 0],
             '-')
    plt.plot(np.arange(SA.in_seq_length, SA.in_seq_length + SA.out_seq_length),
             y_pred[:, i, 0],
             '-', linewidth=0.7, label='mean')
plt.show()