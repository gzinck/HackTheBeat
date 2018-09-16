# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 12:07:31 2018

@author: Denisa
"""
import serial
import numpy as np

from matplotlib import pyplot as plt
from scipy import signal
from scipy import stats
from time import time
from dataresults import DataResults

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:05:33 2018

@author: Denisa
"""

noise_list = ['156\r\n', '72\r\n', '155\r\n', '63\r\n', '222\r\n', '63\r\n', '63\r\n', '238\r\n', '64\r\n', '157\r\n', '189\r\n', '186\r\n', '336\r\n', '160\r\n', '230\r\n', '363\r\n', '213\r\n', '375\r\n', '302\r\n', '242\r\n', '331\r\n', '257\r\n', '263\r\n', '379\r\n', '297\r\n', '421\r\n', '268\r\n', '234\r\n', '337\r\n', '305\r\n', '317\r\n', '313\r\n', '238\r\n', '416\r\n', '263\r\n', '310\r\n', '344\r\n', '281\r\n', '358\r\n', '198\r\n', '231\r\n', '360\r\n', '271\r\n', '345\r\n', '315\r\n', '251\r\n', '422\r\n', '303\r\n', '303\r\n', '381\r\n', '213\r\n', '337\r\n', '306\r\n', '285\r\n', '385\r\n', '306\r\n', '322\r\n', '276\r\n', '257\r\n', '419\r\n', '305\r\n', '229\r\n', '312\r\n', '211\r\n', '352\r\n', '283\r\n', '239\r\n', '347\r\n', '264\r\n', '342\r\n', '339\r\n', '236\r\n', '376\r\n', '276\r\n', '272\r\n', '360\r\n', '276\r\n', '364\r\n', '334\r\n', '260\r\n', '361\r\n', '267\r\n', '264\r\n', '350\r\n', '237\r\n', '379\r\n', '291\r\n', '211\r\n', '345\r\n', '313\r\n', '325\r\n', '349\r\n', '271\r\n', '405\r\n', '258\r\n', '307\r\n', '436\r\n', '309\r\n', '376\r\n', '303\r\n', '248\r\n', '401\r\n', '265\r\n', '311\r\n', '304\r\n', '257\r\n', '354\r\n', '248\r\n', '267\r\n', '376\r\n', '234\r\n', '368\r\n', '310\r\n', '277\r\n', '373\r\n', '272\r\n', '286\r\n', '397\r\n', '288\r\n', '395\r\n', '259\r\n', '274\r\n', '377\r\n', '262\r\n', '307\r\n', '335\r\n', '280\r\n', '382\r\n', '236\r\n', '313\r\n', '383\r\n', '275\r\n', '366\r\n', '263\r\n', '253\r\n', '368\r\n', '208\r\n', '288\r\n', '315\r\n', '301\r\n', '356\r\n', '229\r\n', '256\r\n', '354\r\n', '297\r\n', '399\r\n', '324\r\n', '311\r\n', '403\r\n', '271\r\n', '299\r\n', '313\r\n', '246\r\n', '396\r\n', '253\r\n', '297\r\n', '352\r\n', '260\r\n', '417\r\n', '359\r\n', '333\r\n', '387\r\n', '303\r\n', '293\r\n', '284\r\n', '225\r\n', '379\r\n', '229\r\n', '234\r\n', '368\r\n', '268\r\n', '310\r\n', '329\r\n', '261\r\n', '394\r\n', '246\r\n', '270\r\n', '311\r\n', '235\r\n', '416\r\n', '303\r\n', '273\r\n', '406\r\n', '249\r\n', '291\r\n', '331\r\n', '272\r\n', '354\r\n', '286\r\n', '237\r\n', '345\r\n', '248\r\n', '371\r\n', '296\r\n', '286\r\n', '359\r\n', '272\r\n', '321\r\n', '339\r\n', '263\r\n', '390\r\n', '235\r\n', '300\r\n', '375\r\n', '263\r\n', '316\r\n', '327\r\n', '295\r\n', '381\r\n', '237\r\n', '263\r\n', '313\r\n', '311\r\n', '364\r\n', '283\r\n', '246\r\n', '374\r\n', '256\r\n', '298\r\n', '324\r\n', '217\r\n', '356\r\n', '226\r\n', '260\r\n', '357\r\n', '240\r\n', '346\r\n', '229\r\n', '241\r\n', '370\r\n', '271\r\n', '308\r\n', '366\r\n', '278\r\n', '411\r\n', '245\r\n', '230\r\n', '398\r\n', '250\r\n', '410\r\n', '298\r\n', '268\r\n', '328\r\n', '266\r\n', '270\r\n', '369\r\n', '261\r\n', '396\r\n', '235\r\n', '262\r\n', '346\r\n', '239\r\n', '337\r\n', '337\r\n', '292\r\n', '362\r\n', '271\r\n', '304\r\n', '407\r\n', '284\r\n', '393\r\n', '314\r\n', '236\r\n', '341\r\n', '228\r\n', '322\r\n', '329\r\n', '293\r\n', '384\r\n', '272\r\n', '297\r\n', '405\r\n', '285\r\n', '412\r\n', '301\r\n', '187\r\n', '355\r\n', '227\r\n', '271\r\n', '323\r\n', '265\r\n', '347\r\n', '279\r\n', '243\r\n', '341\r\n', '263\r\n', '353\r\n', '331\r\n', '254\r\n', '378\r\n', '241\r\n', '311\r\n', '331\r\n', '248\r\n', '362\r\n', '263\r\n', '275\r\n', '333\r\n', '262\r\n', '326\r\n', '307\r\n', '248\r\n', '407\r\n', '273\r\n', '267\r\n', '348\r\n', '259\r\n', '369\r\n', '302\r\n', '280\r\n', '423\r\n', '294\r\n', '380\r\n', '339\r\n', '302\r\n', '411\r\n', '264\r\n', '231\r\n', '314\r\n', '220\r\n', '372\r\n', '278\r\n', '284\r\n', '399\r\n', '283\r\n', '345\r\n', '305\r\n', '323\r\n', '346\r\n', '280\r\n', '220\r\n', '422\r\n', '241\r\n', '349\r\n', '342\r\n', '282\r\n', '395\r\n', '235\r\n', '272\r\n', '330\r\n', '243\r\n', '326\r\n', '245\r\n', '238\r\n', '409\r\n', '293\r\n', '372\r\n', '329\r\n', '302\r\n', '401\r\n', '279\r\n', '209\r\n', '333\r\n', '300\r\n', '352\r\n', '256\r\n', '266\r\n', '339\r\n', '190\r\n', '334\r\n', '341\r\n', '192\r\n', '378\r\n', '210\r\n', '235\r\n', '331\r\n', '231\r\n', '352\r\n', '297\r\n', '281\r\n', '392\r\n', '273\r\n', '289\r\n', '393\r\n', '229\r\n', '390\r\n', '217\r\n', '247\r\n', '379\r\n', '243\r\n', '340\r\n', '295\r\n', '215\r\n', '337\r\n', '222\r\n', '255\r\n', '334\r\n', '250\r\n', '357\r\n', '272\r\n', '255\r\n', '396\r\n', '235\r\n', '336\r\n', '328\r\n', '253\r\n', '391\r\n', '290\r\n', '288\r\n', '330\r\n', '307\r\n', '366\r\n', '333\r\n', '260\r\n', '402\r\n', '296\r\n', '326\r\n', '332\r\n', '270\r\n', '380\r\n', '247\r\n', '236\r\n', '299\r\n', '223\r\n', '423\r\n', '261\r\n', '215\r\n', '377\r\n', '241\r\n', '276\r\n', '285\r\n', '251\r\n', '373\r\n', '292\r\n', '268\r\n', '379\r\n', '229\r\n', '266\r\n', '291\r\n', '274\r\n', '361\r\n', '192\r\n', '271\r\n', '372\r\n', '296\r\n', '404\r\n', '328\r\n', '307\r\n', '401\r\n', '280\r\n', '329\r\n', '290\r\n', '259\r\n', '372\r\n', '210\r\n', '260\r\n', '338\r\n', '253\r\n', '360\r\n', '298\r\n', '225\r\n', '359\r\n', '257\r\n', '277\r\n', '313\r\n', '258\r\n', '363\r\n', '272\r\n', '259\r\n', '410\r\n', '237\r\n', '391\r\n', '345\r\n', '279\r\n', '351\r\n', '249\r\n', '326\r\n', '401\r\n', '299\r\n', '397\r\n', '237\r\n', '256\r\n', '388\r\n', '262\r\n', '317\r\n', '322\r\n', '244\r\n', '339\r\n', '204\r\n', '252\r\n', '342\r\n', '244\r\n', '320\r\n', '280\r\n', '251\r\n', '374\r\n', '244\r\n', '345\r\n', '364\r\n', '288\r\n', '382\r\n', '246\r\n', '264\r\n', '316\r\n', '311\r\n', '381\r\n', '212\r\n', '199\r\n', '341\r\n', '289\r\n', '378\r\n', '354\r\n', '329\r\n', '403\r\n', '265\r\n', '226\r\n', '329\r\n', '192\r\n', '313\r\n', '298\r\n', '274\r\n', '418\r\n', '303\r\n', '366\r\n', '394\r\n', '230\r\n', '360\r\n', '349\r\n', '331\r\n', '359\r\n', '259\r\n', '290\r\n', '350\r\n', '394\r\n', '451\r\n', '320\r\n', '317\r\n', '381\r\n', '304\r\n', '352\r\n', '290\r\n', '262\r\n', '349\r\n', '209\r\n', '297\r\n', '230\r\n', '250\r\n', '422\r\n', '223\r\n', '224\r\n', '364\r\n', '265\r\n', '310\r\n', '282\r\n', '280\r\n', '455\r\n', '291\r\n', '273\r\n', '325\r\n', '250\r\n', '372\r\n', '252\r\n', '220\r\n', '330\r\n', '181\r\n', '342\r\n', '301\r\n', '270\r\n', '340\r\n', '204\r\n', '222\r\n', '313\r\n', '282\r\n', '335\r\n', '223\r\n', '277\r\n', '419\r\n', '271\r\n', '355\r\n', '314\r\n', '318\r\n', '423\r\n', '246\r\n', '289\r\n', '369\r\n', '242\r\n', '392\r\n', '250\r\n', '277\r\n', '392\r\n', '233\r\n', '301\r\n', '379\r\n', '172\r\n', '416\r\n', '259\r\n', '271\r\n', '289\r\n', '313\r\n', '434\r\n', '312\r\n', '261\r\n', '386\r\n', '303\r\n', '239\r\n', '405\r\n', '223\r\n', '457\r\n', '171\r\n', '251\r\n', '322\r\n', '262\r\n', '350\r\n', '374\r\n', '279\r\n', '376\r\n', '231\r\n', '234\r\n', '299\r\n', '200\r\n', '381\r\n', '271\r\n', '295\r\n', '415\r\n', '312\r\n', '345\r\n', '368\r\n', '243\r\n', '315\r\n', '230\r\n', '278\r\n', '298\r\n', '302\r\n', '366\r\n', '338\r\n', '252\r\n', '371\r\n', '245\r\n', '317\r\n', '283\r\n', '314\r\n', '401\r\n', '281\r\n', '207\r\n', '316\r\n', '274\r\n', '339\r\n', '342\r\n', '272\r\n', '346\r\n', '164\r\n', '293\r\n', '283\r\n', '297\r\n', '431\r\n', '214\r\n', '169\r\n', '416\r\n', '259\r\n', '360\r\n', '378\r\n', '293\r\n', '363\r\n', '276\r\n', '305\r\n', '393\r\n', '236\r\n', '440\r\n', '341\r\n', '315\r\n', '418\r\n', '340\r\n', '374\r\n', '362\r\n', '305\r\n', '409\r\n', '276\r\n', '268\r\n', '414\r\n', '256\r\n', '376\r\n', '285\r\n', '240\r\n', '370\r\n', '270\r\n', '282\r\n', '324\r\n', '239\r\n', '399\r\n', '275\r\n', '268\r\n', '451\r\n', '240\r\n', '295\r\n', '323\r\n', '290\r\n', '357\r\n', '304\r\n', '366\r\n', '386\r\n', '294\r\n', '386\r\n', '208\r\n', '276\r\n', '423\r\n', '250\r\n', '373\r\n', '354\r\n', '314\r\n', '377\r\n', '181\r\n', '282\r\n', '398\r\n', '208\r\n', '388\r\n', '293\r\n', '235\r\n', '348\r\n', '210\r\n', '290\r\n', '347\r\n', '270\r\n', '371\r\n', '242\r\n', '227\r\n', '348\r\n', '221\r\n', '372\r\n', '352\r\n', '281\r\n', '415\r\n', '269\r\n', '307\r\n', '372\r\n', '311\r\n', '420\r\n', '261\r\n', '292\r\n', '350\r\n', '239\r\n', '324\r\n', '351\r\n', '285\r\n', '386\r\n', '286\r\n', '283\r\n', '347\r\n', '293\r\n', '389\r\n', '234\r\n', '199\r\n', '346\r\n', '242\r\n', '337\r\n', '293\r\n', '292\r\n', '365\r\n', '270\r\n', '241\r\n', '374\r\n', '217\r\n', '387\r\n', '258\r\n', '266\r\n', '376\r\n', '319\r\n', '336\r\n', '362\r\n', '315\r\n', '409\r\n', '236\r\n', '214\r\n', '347\r\n', '289\r\n', '384\r\n', '297\r\n', '241\r\n', '396\r\n', '305\r\n', '313\r\n', '381\r\n', '300\r\n', '423\r\n', '214\r\n', '248\r\n', '364\r\n', '261\r\n', '346\r\n', '304\r\n', '283\r\n', '423\r\n', '251\r\n', '277\r\n', '309\r\n', '231\r\n', '355\r\n', '236\r\n', '206\r\n', '399\r\n', '271\r\n', '334\r\n', '359\r\n', '322\r\n', '402\r\n', '286\r\n', '304\r\n', '359\r\n', '329\r\n', '393\r\n', '326\r\n', '292\r\n', '407\r\n', '268\r\n', '289\r\n', '321\r\n', '223\r\n', '324\r\n', '201\r\n', '245\r\n', '372\r\n', '236\r\n', '382\r\n', '373\r\n', '268\r\n', '371\r\n', '237\r\n', '300\r\n', '366\r\n', '305\r\n', '412\r\n', '228\r\n', '280\r\n', '390\r\n', '305\r\n', '364\r\n', '328\r\n', '248\r\n', '394\r\n', '241\r\n', '283\r\n', '332\r\n', '216\r\n', '364\r\n', '287\r\n', '255\r\n', '375\r\n', '308\r\n', '361\r\n', '390\r\n', '279\r\n', '351\r\n', '239\r\n', '277\r\n', '357\r\n', '299\r\n', '452\r\n', '298\r\n', '221\r\n', '381\r\n', '306\r\n', '318\r\n', '285\r\n', '284\r\n', '379\r\n', '210\r\n', '257\r\n', '389\r\n', '235\r\n', '342\r\n', '353\r\n', '179\r\n', '443\r\n', '310\r\n', '244\r\n', '395\r\n', '311\r\n', '298\r\n', '335\r\n', '264\r\n', '442\r\n', '175\r\n', '376\r\n', '359\r\n', '260\r\n', '420\r\n', '234\r\n', '198\r\n', '320\r\n', '393\r\n', '363\r\n', '234\r\n', '227\r\n', '355\r\n', '303\r\n', '350\r\n', '392\r\n', '294\r\n', '409\r\n', '279\r\n', '254\r\n', '381\r\n', '321\r\n', '408\r\n', '312\r\n', '269\r\n', '403\r\n', '264\r\n', '304\r\n', '346\r\n', '272\r\n', '411\r\n', '297\r\n', '317\r\n', '349\r\n', '197\r\n', '305\r\n', '321\r\n', '251\r\n', '410\r\n', '318\r\n', '319\r\n', '416\r\n', '297\r\n', '343\r\n', '234\r\n', '250\r\n', '394\r\n', '288\r\n', '367\r\n', '307\r\n', '267\r\n', '357\r\n', '264\r\n', '272\r\n', '405\r\n', '240\r\n', '375\r\n', '284\r\n', '298\r\n', '391\r\n', '220\r\n', '266\r\n', '358\r\n', '239\r\n', '389\r\n', '271\r\n', '307\r\n', '392\r\n', '277\r\n', '336\r\n', '313\r\n', '202\r\n', '288\r\n', '209\r\n', '263\r\n', '355\r\n', '221\r\n', '330\r\n', '205\r\n', '187\r\n', '286\r\n', '206\r\n', '316\r\n', '253\r\n', '226\r\n', '394\r\n', '234\r\n', '271\r\n', '359\r\n', '302\r\n', '389\r\n', '269\r\n', '249\r\n', '364\r\n', '252\r\n', '298\r\n', '332\r\n', '232\r\n', '361\r\n', '265\r\n', '248\r\n', '341\r\n', '223\r\n', '347\r\n', '292\r\n', '268\r\n', '374\r\n', '267\r\n', '328\r\n', '369\r\n', '314\r\n', '393\r\n', '270\r\n', '237\r\n', '369\r\n', '246\r\n', '368\r\n', '321\r\n', '280\r\n', '405\r\n', '303\r\n', '304\r\n', '375\r\n', '238\r\n', '394\r\n', '244\r\n', '245\r\n', '318\r\n', '212\r\n', '287\r\n', '310\r\n', '253\r\n', '426\r\n', '307\r\n', '315\r\n', '367\r\n', '226\r\n', '416\r\n', '254\r\n', '236\r\n', '360\r\n', '255\r\n', '344\r\n', '352\r\n', '284\r\n', '390\r\n', '263\r\n', '253\r\n', '368\r\n', '229\r\n', '360\r\n', '299\r\n', '287\r\n', '358\r\n', '250\r\n', '296\r\n', '308\r\n', '264\r\n', '376\r\n', '208\r\n', '249\r\n', '348\r\n', '247\r\n', '347\r\n', '342\r\n', '282\r\n', '374\r\n', '225\r\n', '309\r\n', '348\r\n', '233\r\n', '360\r\n', '271\r\n', '263\r\n', '427\r\n', '266\r\n', '378\r\n', '395\r\n', '307\r\n', '360\r\n', '300\r\n', '297\r\n', '354\r\n', '278\r\n', '364\r\n', '321\r\n', '265\r\n', '363\r\n', '217\r\n', '304\r\n', '329\r\n', '244\r\n', '320\r\n', '206\r\n', '270\r\n', '336\r\n', '226\r\n', '334\r\n', '300\r\n', '249\r\n', '389\r\n', '250\r\n', '311\r\n', '338\r\n', '255\r\n', '367\r\n', '287\r\n', '324\r\n', '411\r\n', '323\r\n', '405\r\n', '344\r\n', '252\r\n', '322\r\n', '196\r\n', '202\r\n', '315\r\n', '241\r\n', '388\r\n', '320\r\n', '239\r\n', '335\r\n', '260\r\n', '318\r\n', '270\r\n', '254\r\n', '427\r\n', '295\r\n', '283\r\n', '347\r\n', '310\r\n', '438\r\n', '347\r\n', '226\r\n', '397\r\n', '257\r\n', '372\r\n', '336\r\n', '242\r\n', '397\r\n', '271\r\n', '276\r\n', '339\r\n', '228\r\n', '321\r\n', '267\r\n', '229\r\n', '321\r\n', '203\r\n', '254\r\n', '344\r\n', '254\r\n', '418\r\n', '262\r\n', '257\r\n', '410\r\n', '261\r\n', '354\r\n', '329\r\n', '207\r\n', '425\r\n', '214\r\n', '263\r\n', '298\r\n', '269\r\n', '395\r\n', '284\r\n', '278\r\n', '393\r\n', '264\r\n', '327\r\n', '325\r\n', '233\r\n', '391\r\n', '276\r\n', '291\r\n', '347\r\n', '250\r\n', '316\r\n', '273\r\n', '237\r\n', '327\r\n', '207\r\n', '255\r\n', '328\r\n', '292\r\n', '389\r\n', '210\r\n', '310\r\n', '371\r\n', '249\r\n', '370\r\n', '336\r\n', '263\r\n', '365\r\n', '271\r\n', '323\r\n', '369\r\n', '280\r\n', '357\r\n', '259\r\n', '265\r\n', '313\r\n', '176\r\n', '339\r\n', '317\r\n', '277\r\n', '392\r\n', '254\r\n', '283\r\n', '358\r\n', '255\r\n', '372\r\n', '299\r\n', '233\r\n', '365\r\n', '283\r\n', '381\r\n', '356\r\n', '272\r\n', '375\r\n', '281\r\n', '268\r\n', '356\r\n', '243\r\n', '297\r\n', '307\r\n', '232\r\n', '308\r\n', '230\r\n', '281\r\n', '288\r\n', '258\r\n', '390\r\n', '233\r\n', '235\r\n', '366\r\n', '224\r\n', '362\r\n', '331\r\n', '269\r\n', '403\r\n', '280\r\n', '326\r\n', '365\r\n', '220\r\n', '422\r\n', '288\r\n', '246\r\n', '397\r\n', '265\r\n', '338\r\n', '332\r\n', '265\r\n', '347\r\n', '234\r\n', '270\r\n', '384\r\n', '261\r\n', '367\r\n', '270\r\n', '236\r\n', '367\r\n', '253\r\n', '308\r\n', '347\r\n', '284\r\n', '350\r\n', '200\r\n', '253\r\n', '353\r\n', '267\r\n', '357\r\n', '284\r\n', '244\r\n', '372\r\n', '274\r\n', '337\r\n', '372\r\n', '247\r\n', '347\r\n', '243\r\n', '251\r\n', '371\r\n', '267\r\n', '363\r\n', '309\r\n', '269\r\n', '404\r\n', '264\r\n', '287\r\n', '353\r\n', '236\r\n', '373\r\n', '245\r\n', '261\r\n', '367\r\n', '255\r\n', '342\r\n', '360\r\n', '272\r\n', '395\r\n', '258\r\n', '293\r\n', '386\r\n', '264\r\n', '364\r\n', '318\r\n', '280\r\n', '366\r\n', '263\r\n', '333\r\n', '369\r\n', '258\r\n', '360\r\n', '255\r\n', '229\r\n', '389\r\n', '231\r\n', '397\r\n', '339\r\n', '259\r\n', '365\r\n', '273\r\n', '282\r\n', '345\r\n', '244\r\n', '367\r\n', '216\r\n', '264\r\n', '383\r\n', '209\r\n', '358\r\n', '312\r\n', '252\r\n', '342\r\n', '239\r\n', '255\r\n', '343\r\n', '265\r\n', '399\r\n', '313\r\n', '256\r\n', '351\r\n', '248\r\n', '338\r\n', '310\r\n', '249\r\n', '333\r\n', '287\r\n', '292\r\n', '368\r\n', '249\r\n', '353\r\n', '370\r\n', '283\r\n', '363\r\n', '286\r\n', '293\r\n', '376\r\n', '294\r\n', '414\r\n', '240\r\n', '273\r\n', '357\r\n', '286\r\n', '406\r\n', '284\r\n', '233\r\n', '345\r\n', '232\r\n', '252\r\n', '287\r\n', '264\r\n', '384\r\n', '238\r\n', '267\r\n', '366\r\n', '328\r\n', '358\r\n', '333\r\n', '284\r\n', '364\r\n', '269\r\n', '245\r\n', '406\r\n', '271\r\n', '339\r\n', '270\r\n', '252\r\n', '384\r\n', '264\r\n', '335\r\n', '319\r\n', '273\r\n', '365\r\n', '197\r\n', '275\r\n', '394\r\n', '273\r\n', '373\r\n', '308\r\n', '208\r\n', '408\r\n', '241\r\n', '334\r\n', '327\r\n', '316\r\n', '427\r\n', '268\r\n', '297\r\n', '386\r\n', '239\r\n', '310\r\n', '309\r\n', '238\r\n', '353\r\n', '225\r\n', '308\r\n', '363\r\n', '259\r\n', '341\r\n', '270\r\n', '233\r\n', '303\r\n', '239\r\n', '334\r\n', '353\r\n', '247\r\n', '364\r\n', '315\r\n', '320\r\n', '346\r\n', '277\r\n', '374\r\n', '276\r\n', '217\r\n', '315\r\n', '215\r\n', '347\r\n', '340\r\n', '249\r\n', '317\r\n', '249\r\n', '249\r\n', '366\r\n', '268\r\n', '392\r\n', '301\r\n', '232\r\n', '400\r\n', '254\r\n', '337\r\n', '349\r\n', '325\r\n', '430\r\n', '306\r\n', '340\r\n', '403\r\n', '292\r\n', '373\r\n', '292\r\n', '258\r\n', '368\r\n', '236\r\n', '295\r\n', '374\r\n', '236\r\n', '318\r\n', '267\r\n', '248\r\n', '366\r\n', '226\r\n', '331\r\n', '363\r\n', '245\r\n', '361\r\n', '248\r\n', '267\r\n', '355\r\n', '206\r\n', '356\r\n', '264\r\n', '235\r\n', '406\r\n', '277\r\n', '343\r\n', '375\r\n', '240\r\n', '355\r\n', '254\r\n', '205\r\n', '365\r\n', '215\r\n', '307\r\n', '266\r\n', '365\r\n', '364\r\n', '237\r\n', '295\r\n', '365\r\n', '291\r\n', '367\r\n', '256\r\n', '226\r\n', '349\r\n', '245\r\n', '372\r\n', '331\r\n', '295\r\n', '364\r\n', '292\r\n', '279\r\n', '343\r\n', '273\r\n', '318\r\n', '288\r\n', '238\r\n', '367\r\n', '258\r\n', '330\r\n', '339\r\n', '277\r\n', '422\r\n', '265\r\n', '291\r\n', '361\r\n', '279\r\n', '346\r\n', '276\r\n', '244\r\n', '384\r\n', '290\r\n', '334\r\n', '332\r\n', '209\r\n', '372\r\n', '215\r\n', '270\r\n', '343\r\n', '219\r\n', '354\r\n', '353\r\n', '249\r\n', '403\r\n', '277\r\n', '265\r\n', '334\r\n', '252\r\n', '371\r\n', '236\r\n', '247\r\n', '369\r\n', '263\r\n', '342\r\n', '321\r\n', '248\r\n', '363\r\n', '243\r\n', '244\r\n', '337\r\n', '231\r\n', '355\r\n', '298\r\n', '269\r\n', '344\r\n', '254\r\n', '416\r\n', '342\r\n', '243\r\n', '318\r\n', '243\r\n', '240\r\n', '330\r\n', '289\r\n', '359\r\n', '326\r\n', '268\r\n', '384\r\n', '245\r\n', '280\r\n', '319\r\n', '291\r\n', '337\r\n', '228\r\n', '274\r\n', '380\r\n', '265\r\n', '385\r\n', '297\r\n', '245\r\n', '367\r\n', '239\r\n', '264\r\n', '344\r\n', '259\r\n', '379\r\n', '279\r\n', '249\r\n', '400\r\n', '266\r\n', '341\r\n', '316\r\n', '217\r\n', '372\r\n', '247\r\n', '274\r\n', '365\r\n', '308\r\n', '373\r\n', '298\r\n', '285\r\n', '376\r\n', '256\r\n', '290\r\n', '341\r\n', '272\r\n', '386\r\n', '254\r\n', '282\r\n', '350\r\n', '239\r\n', '379\r\n', '309\r\n', '295\r\n', '404\r\n', '243\r\n', '305\r\n', '349\r\n', '250\r\n', '393\r\n', '263\r\n', '263\r\n', '331\r\n', '206\r\n', '372\r\n', '346\r\n', '246\r\n']
beat_list = ['-1\r\n', '-11\r\n', '-5\r\n', '-26\r\n', '-51\r\n', '-27\r\n', '-40\r\n', '53\r\n', '54\r\n', '43\r\n', '-37\r\n', '110\r\n', '89\r\n', '0\r\n', '83\r\n', '-27\r\n', '-76\r\n', '-40\r\n', '1\r\n', '-25\r\n', '19\r\n', '7\r\n', '3\r\n', '5\r\n', '24\r\n', '2\r\n', '-18\r\n', '-13\r\n', '4\r\n', '4\r\n', '6\r\n', '-1\r\n', '-11\r\n', '-5\r\n', '-26\r\n', '-51\r\n', '-27\r\n', '-40\r\n', '53\r\n', '54\r\n', '0\r\n', '-152\r\n', '-175\r\n', '-93\r\n', '-57\r\n', '-69\r\n', '-46\r\n', '-37\r\n', '-69\r\n', '82\r\n', '-7\r\n', '44\r\n', '82\r\n', '106\r\n', '-16\r\n', '58\r\n', '-77\r\n', '-76\r\n', '-74\r\n', '-28\r\n', '-34\r\n', '-48\r\n', '-19\r\n', '10\r\n', '29\r\n', '24\r\n', '31\r\n', '16\r\n', '-15\r\n', '-10\r\n', '-14\r\n', '12\r\n', '17\r\n', '7\r\n', '-6\r\n', '7\r\n', '-6\r\n', '-59\r\n', '-35\r\n', '-54\r\n', '26\r\n', '-28\r\n', '20\r\n', '61\r\n', '12\r\n', '70\r\n', '21\r\n', '25\r\n', '51\r\n', '-53\r\n', '-12\r\n', '-15\r\n', '-11\r\n', '35\r\n', '-42\r\n', '1\r\n', '-55\r\n', '-48\r\n', '20\r\n', '41\r\n', '9\r\n', '-30\r\n', '-11\r\n', '0\r\n', '9\r\n', '25\r\n', '20\r\n', '6\r\n', '-16\r\n', '-2\r\n', '11\r\n', '13\r\n', '35\r\n', '3\r\n', '-13\r\n', '0\r\n', '97\r\n', '-36\r\n', '46\r\n', '15\r\n', '-7\r\n', '25\r\n', '-67\r\n', '-60\r\n', '-22\r\n', '53\r\n', '49\r\n', '-51\r\n', '66\r\n', '64\r\n', '96\r\n', '80\r\n', '-77\r\n', '33\r\n', '-82\r\n', '-114\r\n', '-17\r\n', '-50\r\n', '4\r\n', '42\r\n', '-2\r\n', '-47\r\n', '-18\r\n', '-8\r\n', '8\r\n', '23\r\n', '9\r\n', '-22\r\n', '5\r\n', '16\r\n', '19\r\n', '-9\r\n', '9\r\n', '6\r\n', '-22\r\n', '88\r\n', '-39\r\n', '-28\r\n', '84\r\n', '-42\r\n', '2\r\n', '-65\r\n', '75\r\n', '10\r\n', '-11\r\n', '6\r\n', '-65\r\n', '73\r\n', '-39\r\n', '2\r\n', '91\r\n', '6\r\n', '-39\r\n', '69\r\n', '-56\r\n', '-91\r\n', '-54\r\n', '32\r\n', '26\r\n', '-35\r\n', '-39\r\n', '-39\r\n', '-24\r\n', '31\r\n', '62\r\n', '18\r\n', '-1\r\n', '22\r\n', '-13\r\n', '-7\r\n', '-6\r\n', '-20\r\n', '2\r\n', '4\r\n', '105\r\n', '-27\r\n', '-28\r\n', '-12\r\n', '95\r\n', '-33\r\n', '-17\r\n', '74\r\n', '-2\r\n', '7\r\n', '44\r\n', '-15\r\n', '73\r\n', '-59\r\n', '-38\r\n', '69\r\n', '-56\r\n', '21\r\n', '-61\r\n', '66\r\n', '-52\r\n', '-83\r\n', '-48\r\n', '45\r\n', '16\r\n', '-26\r\n', '-8\r\n', '-19\r\n', '-18\r\n', '3\r\n', '28\r\n', '3\r\n', '21\r\n', '25\r\n', '17\r\n', '-6\r\n', '-8\r\n', '-18\r\n', '14\r\n', '-50\r\n', '-65\r\n', '-59\r\n', '73\r\n', '22\r\n', '31\r\n', '116\r\n', '-24\r\n', '3\r\n', '-34\r\n', '24\r\n', '27\r\n', '-53\r\n', '-73\r\n', '-23\r\n', '-48\r\n', '36\r\n', '-24\r\n', '-42\r\n', '111\r\n', '-4\r\n', '28\r\n', '-37\r\n', '45\r\n', '49\r\n', '21\r\n', '9\r\n', '-20\r\n', '-37\r\n', '-25\r\n', '-32\r\n', '10\r\n', '19\r\n', '11\r\n', '18\r\n', '11\r\n', '29\r\n', '-1\r\n', '-5\r\n', '-6\r\n', '23\r\n', '-23\r\n', '-34\r\n', '94\r\n', '-27\r\n', '-15\r\n', '-59\r\n', '74\r\n', '30\r\n', '-20\r\n', '17\r\n', '-54\r\n', '82\r\n', '-25\r\n', '44\r\n', '101\r\n', '106\r\n', '2\r\n', '-96\r\n', '-21\r\n', '-87\r\n', '-11\r\n', '46\r\n', '0\r\n', '-56\r\n', '-18\r\n', '-25\r\n', '-15\r\n', '12\r\n', '1\r\n', '43\r\n', '8\r\n', '-14\r\n', '4\r\n', '-17\r\n', '-15\r\n', '-8\r\n', '-10\r\n', '-9\r\n', '97\r\n', '-33\r\n', '-71\r\n', '-73\r\n', '27\r\n', '-34\r\n', '-44\r\n', '81\r\n', '21\r\n', '52\r\n', '76\r\n', '13\r\n', '90\r\n', '-49\r\n', '-12\r\n', '77\r\n', '-55\r\n', '59\r\n', '-41\r\n', '61\r\n', '-65\r\n', '-81\r\n', '-53\r\n', '-6\r\n', '7\r\n', '-49\r\n', '-16\r\n', '35\r\n', '27\r\n', '8\r\n', '17\r\n', '-20\r\n', '-4\r\n', '-31\r\n', '-13\r\n', '22\r\n', '12\r\n', '4\r\n', '-2\r\n', '-51\r\n', '90\r\n', '-24\r\n', '-61\r\n', '8\r\n', '26\r\n', '113\r\n', '-26\r\n', '-2\r\n', '-59\r\n', '35\r\n', '53\r\n', '-46\r\n', '-74\r\n', '5\r\n', '-44\r\n', '66\r\n', '-26\r\n', '-19\r\n', '104\r\n', '-21\r\n', '8\r\n', '-52\r\n', '50\r\n', '59\r\n', '-11\r\n', '-22\r\n', '-16\r\n', '12\r\n', '8\r\n', '0\r\n', '-7\r\n', '8\r\n', '14\r\n', '-15\r\n', '-8\r\n', '-18\r\n', '-8\r\n', '9\r\n', '8\r\n', '-19\r\n', '-7\r\n', '-37\r\n', '95\r\n', '-25\r\n', '-45\r\n', '79\r\n', '101\r\n', '24\r\n', '-10\r\n', '-14\r\n', '-80\r\n', '62\r\n', '-14\r\n', '22\r\n', '88\r\n', '26\r\n', '-58\r\n', '52\r\n', '-70\r\n', '-102\r\n', '-46\r\n', '25\r\n', '-17\r\n', '-56\r\n', '-16\r\n', '2\r\n', '4\r\n', '23\r\n', '26\r\n', '-6\r\n', '6\r\n', '-3\r\n', '17\r\n', '-28\r\n', '-17\r\n', '7\r\n', '25\r\n', '18\r\n', '106\r\n', '-31\r\n', '-31\r\n', '13\r\n', '96\r\n', '-42\r\n', '-6\r\n', '70\r\n', '-35\r\n', '-4\r\n', '36\r\n', '12\r\n', '78\r\n', '-63\r\n', '-10\r\n', '70\r\n', '-65\r\n', '27\r\n', '-74\r\n', '-4\r\n', '-73\r\n', '-82\r\n', '-36\r\n', '55\r\n', '25\r\n', '-34\r\n', '-16\r\n', '3\r\n', '25\r\n', '2\r\n', '2\r\n', '40\r\n', '37\r\n', '-46\r\n', '-15\r\n', '19\r\n', '33\r\n', '-9\r\n', '10\r\n', '-57\r\n', '-71\r\n', '-65\r\n', '57\r\n', '24\r\n', '58\r\n', '122\r\n', '-27\r\n', '4\r\n', '-55\r\n', '6\r\n', '26\r\n', '-52\r\n', '-71\r\n', '-31\r\n', '-49\r\n', '65\r\n', '-17\r\n', '-43\r\n', '107\r\n', '-9\r\n', '29\r\n', '-39\r\n', '18\r\n', '53\r\n', '28\r\n', '-30\r\n', '-35\r\n', '-4\r\n', '16\r\n', '26\r\n', '3\r\n', '-17\r\n', '-5\r\n', '27\r\n', '1\r\n', '-4\r\n', '-16\r\n', '-1\r\n', '15\r\n', '-47\r\n', '3\r\n', '-42\r\n', '99\r\n', '-19\r\n', '-26\r\n', '97\r\n', '97\r\n', '28\r\n', '-22\r\n', '-10\r\n', '-77\r\n', '-89\r\n', '15\r\n', '52\r\n', '-23\r\n', '90\r\n', '19\r\n', '14\r\n', '68\r\n', '-54\r\n', '-37\r\n', '26\r\n', '0\r\n', '-44\r\n', '-39\r\n', '-24\r\n', '0\r\n', '0\r\n', '23\r\n', '23\r\n', '-10\r\n', '-14\r\n', '13\r\n', '2\r\n', '3\r\n', '-5\r\n', '-3\r\n', '-12\r\n', '90\r\n', '113\r\n', '-15\r\n', '-91\r\n', '-70\r\n', '-86\r\n', '-13\r\n', '78\r\n', '11\r\n', '51\r\n', '30\r\n', '4\r\n', '83\r\n', '51\r\n', '22\r\n', '66\r\n', '-80\r\n', '2\r\n', '-90\r\n', '43\r\n', '-69\r\n', '-56\r\n', '-51\r\n', '0\r\n', '-15\r\n', '-60\r\n', '-9\r\n', '19\r\n', '41\r\n', '16\r\n', '4\r\n', '29\r\n', '10\r\n', '-4\r\n', '-12\r\n', '-7\r\n', '-12\r\n', '-33\r\n', '-26\r\n', '-55\r\n', '96\r\n', '-7\r\n', '-14\r\n', '-54\r\n', '0\r\n', '112\r\n', '-17\r\n', '17\r\n', '-35\r\n', '30\r\n', '36\r\n', '-49\r\n', '-71\r\n', '-10\r\n', '-45\r\n', '75\r\n', '-11\r\n', '24\r\n', '76\r\n', '0\r\n', '-12\r\n', '-61\r\n', '34\r\n', '35\r\n', '23\r\n', '-13\r\n', '-42\r\n', '-15\r\n', '12\r\n', '-4\r\n', '12\r\n', '9\r\n', '18\r\n', '15\r\n', '-12\r\n', '-8\r\n', '-6\r\n', '-4\r\n', '3\r\n', '-52\r\n', '32\r\n', '-28\r\n', '89\r\n', '-27\r\n', '-40\r\n', '-62\r\n', '68\r\n', '30\r\n', '10\r\n', '23\r\n', '-25\r\n', '-63\r\n', '86\r\n', '39\r\n', '-5\r\n', '1\r\n', '33\r\n', '-6\r\n', '-5\r\n', '-66\r\n', '-37\r\n', '5\r\n', '27\r\n', '-13\r\n', '7\r\n', '-31\r\n', '2\r\n', '53\r\n', '0\r\n', '-9\r\n', '-7\r\n', '4\r\n', '-21\r\n', '-3\r\n', '-8\r\n', '34\r\n', '-3\r\n', '2\r\n', '-52\r\n', '-63\r\n', '-58\r\n', '-47\r\n', '52\r\n', '2\r\n', '60\r\n', '65\r\n', '21\r\n', '58\r\n', '54\r\n', '16\r\n', '91\r\n', '84\r\n', '72\r\n', '-78\r\n', '-118\r\n', '-51\r\n', '-84\r\n', '3\r\n', '-52\r\n'] 

def data_collection():
    ser = serial.Serial('COM3', 9600)
    value_list = [] 
    start = time()
    while start < 11:
        value = ser.readline()
        num = value.decode('utf-8')
        value_list.append(num) 
    imgdata=plt.plot(value_list)     
    plt.savefig(imgdata, format='png')

    integer_list=[]
    for i in value_list:
        integer_list.append(int(i))
    peak= scipy.signal.find_peaks_cwt(integer_list, [1], noise_perc=99)
    peak_diff= np.diff(peak)
    
    stat_info= stats.ks_2samp(noise_diff, beat_diff)

    return DataResults("imgdata.png", stat_info, 0)

    
    
plt.plot(noise_integer_list[:700])
plt.scatter(noise_peak[:700],np.zeros(len(noise_peak[:700])))
    

    """
    ser = serial.Serial('COM3', 9600)
    value_list = []  
    while True:
        value = ser.readline()
        num = value.decode('utf-8')
        #y=int(num)
        #print(num)
        value_list.append(num)
    """
#plt.plot(noise_list)
noise_integer_list=[]

for i in noise_list:
    noise_integer_list.append(int(i))
    
noise_peak= scipy.signal.find_peaks_cwt(noise_integer_list[:700], [1], noise_perc=99)
noise_diff= np.diff(noise_peak)
plt.plot(noise_integer_list[:700])
plt.scatter(noise_peak[:700],np.zeros(len(noise_peak[:700])))
plt.show()

##############################################
beat_integer_list=[]

for i in beat_list:
    beat_integer_list.append(int(i))
    
beat_peak= scipy.signal.find_peaks_cwt(beat_integer_list, [1], noise_perc=99)
beat_diff=np.diff(beat_peak)
image=plt.plot(beat_integer_list)
plt.scatter(beat_peak,150*np.ones(len(beat_peak)))
plt.show()

print(stats.ks_2samp(noise_diff, beat_diff))