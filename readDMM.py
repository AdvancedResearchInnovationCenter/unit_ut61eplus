
import logging
from ut61eplus import UT61EPLUS
import time 
log = logging.getLogger(__name__)

# logging.basicConfig(level=logging.DEBUG)

dmm = UT61EPLUS()


t = 0
n = 0
now = time.time()
while True:
    # log.info('name=%s', dmm.getName())
    # dmm.sendCommand('lamp')
    # dmm.takeMeasurement()
    m = dmm.takeMeasurement()
    n += 1
    t += time.time() - now
    now = time.time()
    if n % 10 == 0:
        print('n=%d, t=%f, t/n=%f' % (n, t, t/n))
    # log.info('measurent=%s', m)
    # print(m.display_decimal, m.display_unit, m.mode)