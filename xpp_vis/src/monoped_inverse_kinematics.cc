
#include <xpp_vis/mono/monoped_inverse_kinematics.h>

#include <cmath>
#include <iostream>

#include <xpp_vis/mono/hyqleg_inverse_kinematics.h>

namespace xpp {
namespace mono {

MonopedInverseKinematics::MonopedInverseKinematics ()
{
}

Joints
MonopedInverseKinematics::GetAllJointAngles(const EndeffectorsPos& x_B) const
{
  HyqlegInverseKinematics leg;

  Eigen::Vector3d offset_base_to_hip(0.0, 0.0, 0.15);
  Eigen::VectorXd q0 = leg.GetJointAngles(x_B.At(E0) + offset_base_to_hip);

  return Joints({q0});
}

MonopedInverseKinematics::~MonopedInverseKinematics ()
{
}

} /* namespace mono */
} /* namespace xpp */

