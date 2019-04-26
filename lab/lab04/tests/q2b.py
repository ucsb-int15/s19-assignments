test = {   'name': 'q2b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> diabetes_mean.size\n10',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.all(np.isclose(diabetes_mean, '
                                               '[0]*10))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.all(np.isclose(np.zeros(10), '
                                               'np.mean(normalized_features, '
                                               'axis=0))) # make sure data is '
                                               'centered at 0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> -.003 < '
                                               'np.sum(normalized_features[0]) '
                                               '< 0.003 # make sure scaling '
                                               'was done correctly\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
