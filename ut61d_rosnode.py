from ut61eplus import UT61EPLUS
import rospy
from std_msgs.msg import Float64

rospy.init_node('ut61d', anonymous=True)

ohm_pub = rospy.Publisher('/piezo', Float64)
dmm = UT61EPLUS()

while True:
# log.info('name=%s', dmm.getName())
# dmm.sendCommand('lamp')
# dmm.takeMeasurement()
    m = dmm.takeMeasurement()
    kiloohm = m.display_decimal
    kiloohm = float(kiloohm)
    kiloohm = Float64(kiloohm)

    ohm_pub.publish(kiloohm)
