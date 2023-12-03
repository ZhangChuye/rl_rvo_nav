# Meaning of RESULTS in results.txt

---

results.txt 
"policy_name: r6_1_50  successful rate: 95.00% average EpLen: 77.21 std length 7.03 average speed: 1.11 std speed 0.09"

---


1. **policy_name**: This is the name of the policy. For example, "r6_1_50" might refer to a policy saved at a specific epoch or iteration during training. The naming convention likely encodes information about the training conditions or version of the policy.

---

2. **successful rate**: This is the percentage of episodes where the policy was successful in achieving its goal. A higher success rate indicates a more effective policy. For example, "95.00%" means the policy successfully completed its objective in 95% of the episodes.

---

3. **average EpLen** (Average Episode Length): This is the average number of steps taken per episode. It gives an idea of how long it takes for the policy to reach its goal, on average. For example, "77.21" means that, on average, it takes 77.21 steps to complete an episode.

---

4. **std length** (Standard Deviation of Episode Length): This number indicates the variability in the length of episodes. A lower standard deviation means the episode lengths are more consistent. For example, "7.03" suggests there is some variation in how quickly the policy completes its objective.

---

5. **average speed**: This metric likely represents the average speed of the agent (or agents) controlled by the policy throughout an episode. For instance, "1.11" could mean the agent moves at an average speed of 1.11 units per time step (the exact units depend on the environment's configuration).

---

6. **std speed** (Standard Deviation of Speed): Similar to the standard deviation of episode length, this indicates the variability in the agent's speed. A lower number suggests more consistent speed throughout episodes

---