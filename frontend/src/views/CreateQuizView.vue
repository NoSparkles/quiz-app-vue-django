<template>
  <div class="create-quiz">
    <div class="home-link">
      <RouterLink to="/">Home</RouterLink>
    </div>
    <CreateForm />
  </div>
</template>

<script>
import CreateForm from '@/components/CreateForm.vue';


export default {
  components: {
    CreateForm
  }
}
</script>

<style>
.create-quiz .home-link {
  margin-top: 20px;
}

.create-quiz .home-link>a {
  margin-top: 20px;
  color: black;
  font-size: 2em;
  align-self: start;
  margin-left: 40px;
  border-radius: 12px;
  position: relative;
  transition: 0.1s ease;
}

.create-quiz .home-link>a::after {
  content: "";
  width: 0;
  background-color: rgb(94, 158, 255);
  height: 3px;
  position: absolute;
  left: 50%;
  bottom: 0;
  transform: translateX(-50%);
  margin: auto;
  transition: 0.3s ease;
}

.create-quiz .home-link>a:hover::after {
  width: 100%;
}
</style>