random_data = [
    'GgPOrkGyWTSqm', 'bfVTQFBAhIinRfaWHbq', 'DBectpWwHT', 'MMeociJaZxrCxf', 'zmggnyfHPPGljNvCQagD', 'ovlbVDMIAVQvKOS', 'KxptLDEYcyZWML', 'cFrhoqQsITgrLBmsbg', 'zjojoXVBIdbydDdN', 'qewJSKCBJWVdaVjnkQTU',
    'GhJlOoCkzdpB', 'ZtiGMhqLQojY', 'BcJHTzTJPqbBCLiI', 'DtrrRQNoXsdEQ', 'JBWFMocTwEaJtGVQWXqS', 'ytsUszUPuQrhwOeBHP', 'zKyxiAnKhLS', 'iqPbotQByCSwTxowsZ', 'qmMYujyzAXVr', 'iUWqhOLdlBaRrYs',
    'slBgBGLneo', 'SoLkUFlsEzV', 'UbePpUfojnCjIbJF', 'EgQxgPDOmwhzmLE', 'vDAWzoQwsrThN', 'TCCpLKlNXcIFDt', 'yqYXSsDqnpCl', 'RcEVhnWMlNdMbXRpw', 'PLreLUJEWiu', 'GtDrOkAqqKTh',
    'McqZmQwxuIYKgRtTOZ', 'ShEPGVcYLPVCdTjl', 'LJRkHviAVVIaJ', 'oTeiJGXVRaEXsoSHmCx', 'TCFMWcVNdEbiMHTai', 'QUQfmshWijChwT', 'kKPZAEnBizUk', 'knYGzjzVMpwuPW', 'IMUygmgTUVBNC', 'CztDXUedmKUKLFFzdyn',
    'kPCcKJGwRrEc', 'kaBxnOuxgSTUSENfLf', 'RBBzvlrrOsjFdTSrcKJy', 'caeSmoeBAClAHKVy', 'zSpoazMtjkWaTevpkIAw', 'dTuoqelDOvxfnDXl', 'WFYqVwzLAdyLkgWjMY', 'VZiNbkPKyTdSB', 'EdWGlgwlehdpwwaWQanS', 'WiwNVSwvXskswANqck',
    'fIlBHbQVdIEarTkH', 'LHAmAISOCsCOha', 'QOjCScEnLBWrzUGad', 'dNdPvTLVQZxDuXVxxOlK', 'crRorhGwfcVnSJZJRaIn', 'SLgOmawQrVujJQevrql', 'wJEuCqRSGAV', 'mVRhHMeJaHWL', 'fyEeQIFcKaJdLn', 'tnSPGVazwtzIutuHqSH',
    'ZxKweQnguxIluqRALY', 'HPGBSkhihsXtAe', 'HOKsQDZDUyF', 'WJYvIrPSKIzB', 'nOkPtVIVWTvPteIsb', 'avJtSNLNdfpYUgQJTZ', 'VfjhGvgOFjtQpLkH', 'GscNYZdgjFlKbVg', 'YdnqGKbXEJc', 'WmCjBnGrqvT',
    'LInUlnqcHqrIbx', 'dnXMyikTnuoVGN', 'nkQjWTEZGONWWReHDG', 'hxHPhRlTgP', 'EdAKHESqxQvzvlABYHf', 'gwNwwIIQLLzwvbOTqfUM', 'bMbkuVHsSN', 'wWAHjIEKsRVTDwWpRJC', 'MoWbpSGQzIYXDRSvDEG', 'UDDlCLaTbRdMXcClW',
    'YEVPmnaTsPDi', 'fIDZziSjYomhpnsYZeNT', 'VGnmQicvPPuUIpOf', 'PyWteiXtEqUoNJqQr', 'PZmWeLMuYdpU', 'qdbJwtxGHGUpSmQpQGnG', 'aLXlmYaNXYc', 'aVEuMZsKEaUkzo', 'ZqOCUQpOUOGaZTe', 'CLffVVrESxecDjQQuAzR',
    'bhJslsrRIXBWZUaCOI', 'rwIWVTEyRMJoLQOprqk', 'dlCLBURIgVfMzuSdno', 'bJfycTLdmIAHvOLgHS', 'ZdECejfuaXW', 'lXvtPenkjnwEZTFMr', 'FPbpGVQcCpUVAVYIT', 'OgurXIDBYbQPqNzZyb', 'PfkHAlOYqGt', 'vebVRSWvYLFtM'
]
random_patterns = [f"{pat}.py" for pat in random_data]


import pathlib
import time

path = pathlib.Path(".")

t0 = time.perf_counter()

for pat in random_data:
    list(path.rglob(pat))

print(time.perf_counter() - t0)
