<template>
  <router-view v-slot="{ Component }">
    <Transition name="route" mode="out-in">
      <component :is="Component"></component>
    </Transition>
  </router-view>
</template>

<style>
* {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  overflow-x: hidden;
}

.route-enter-from {
  opacity: 0;
  transform: translateY(50px);
}

.route-enter-active {
  transition: 0.1s ease-out;
}

.route-leave-to {
  opacity: 0;
  transform: translateY(-50px);
}

.route-leave-active {
  transition: 0.1s ease-out;
}
</style>
