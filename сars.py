import pandas as pd
import pickle


def cars_predict(brand, fuel='gas', asp='std', carlen=174 * 2.54, cnum=4, esz=127,
                 hpw=104, peakrpm=5130, hwmpg=30.8, symb=1, cbd='sedan', dvw='fwd',
                 et='ohc', fs='mpfi'):
    # brand - название фирмы машины, на английском, размер букв не важен (заглавная/строчная/etc)
    # fuel - либо 'gas', либо 'diesel'
    # aspiration - наддув, std или турбо
    # carlength - длина машины в см
    # cnum (cylindernumber) - количество цилиндров
    # esz (enginesize) - объем двигателя автомобиля
    # hpw (horsepower) - количество лошадиных сил
    # peakrpm - максимальное число оборотов
    # hwmpg (highwaympg) - Расход топлива (мили/галлон, mpg)
    # symb - страховая опасность автомобиля, где -2 - самый безопасный автомобиль, +3 - самый опасный
    # cbd (carbody) - тип автомобиля, варианты: sedan, hatchback, convertible, hardtop, wagon
    # dvw (drivewheel) - ведущее колесо, 4wd, fwd или rwd
    # et (enginetype) - тип двигателя, dohc, dohcv, l, ohc, ohcv, ohcf или rotor
    # fs (fuelsystem) - топливная система, 1bbl, 2bbl, 4bbl, idi, mfi, mpfi, spdi или spfi
    segment0 = ['chevrolet', 'dodge', 'plymouth', 'honda', 'subaru', 'isuzu']
    segment1 = ['mitsubishi', 'renault', 'toyota', 'volkswagen', 'nissan', 'mazda']
    segment2 = ['saab', 'peugeot', 'alfa-romero', 'mercury', 'audi', 'volvo']
    segment3 = ['bmw', 'porsche', 'buick', 'jaguar']
    # print((brand in segment1)*1 + 2*(brand in segment2) + 3*(brand in segment3))
    loaded_model = pickle.load(open('Auto.pkl', 'rb'))
    data = {
        'segment': [(brand in segment1) * 1 + 2 * (brand in segment2) + 3 * (brand in segment3)],
        'fuel': [int((fuel == 'gas'))],
        'aspiration': [int((asp == 'std'))],
        'carlength': [carlen / 2.54],
        'cylindernumber': [cnum],
        'enginesize': [esz],
        'horsepower': [hpw],
        'peakrpm': [peakrpm],
        'highwaympg': [hwmpg],
        'symboling_Moderately_Risky': [int(symb == 2)],
        'symboling_Moderately_Safe': [int(symb == -1)],
        'symboling_Neutral': [int(symb == 1)],
        'symboling_Safe': [int(symb == 0)],
        'symboling_Very_Risky': [int(symb == 3)],
        'symboling_Very_Safe': [int(symb == -2)],
        'carbody_convertible': [int(cbd == 'convertible')],
        'carbody_hardtop': [int(cbd == 'hardtop')],
        'carbody_hatchback': [int(cbd == 'hatchback')],
        'carbody_sedan': [int(cbd == 'sedan')],
        'carbody_wagon': [int(cbd == 'wagon')],
        'drivewheel_4wd': [int(dvw == '4wd')],
        'drivewheel_fwd': [int(dvw == 'fwd')],
        'drivewheel_rwd': [int(dvw == 'rwd')],
        'enginetype_dohc': [int(et == 'dohc')],
        'enginetype_dohcv': [int(et == 'dohcv')],
        'enginetype_l': [int(et == 'l')],
        'enginetype_ohc': [int(et == 'ohc')],
        'enginetype_ohcf': [int(et == 'ohcf')],
        'enginetype_ohcv': [int(et == 'ohcv')],
        'enginetype_rotor': [int(et == 'rotor')],
        'fuelsystem_1bbl': [int(fs == '1bbl')],
        'fuelsystem_2bbl': [int(fs == '2bbl')],
        'fuelsystem_4bbl': [int(fs == '4bbl')],
        'fuelsystem_idi': [int(fs == 'idi')],
        'fuelsystem_mfi': [int(fs == 'mfi')],
        'fuelsystem_mpfi': [int(fs == 'mpfi')],
        'fuelsystem_spdi': [int(fs == 'spdi')],
        'fuelsystem_spfi': [int(fs == 'spfi')]
    }
    df = pd.DataFrame(data)
    return loaded_model.predict(df)
