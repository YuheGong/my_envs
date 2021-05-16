from gym.envs.registration import register

register(
    id='MyRobot-v0',
    entry_point='my_envs.mujoco.myrobot:MyRobotEnv',
)
