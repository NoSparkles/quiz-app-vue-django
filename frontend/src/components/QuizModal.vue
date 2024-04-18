<template>
  <div class="quiz-modal-wrapper" @click.self="() => handleClick('close')">
    <div ref="el" class="quiz-modal">
      <h1>{{ title }}</h1>
      <p>Number of questions: {{ numOfQuestions }}</p>
      <button @click="$emit('start')">Start <span class="span1" /><span class="span2" /></button>
      <button @click.self="() => {
        handleClick('delete')
      }" class="delete-quiz">Delete<span class="span1" /><span class="span2" /></button>
    </div>
  </div>
</template>

<script>
import gsap from 'gsap'
import { ref, onMounted } from 'vue'
export default {
  props: [
    'title',
    'numOfQuestions'
  ],
  setup(props, { emit }) {
    const el = ref(null)
    onMounted(() => {
      gsap.fromTo(el.value, {
        scale: 1.2
      }, {
        scale: 1,
        duration: 0.2,
      })
    })
    const handleClick = (event) => {
      gsap.fromTo(el.value, {
        opacity: 1,
        scale: 1
      }, {
        opacity: 0,
        scale: 1.2,
        duration: 0.2
      })
      setTimeout(() => {
        emit(event)
      }, 200);
    }
    return {
      el,
      handleClick
    }
  }
}
</script>

<style>
.quiz-modal-wrapper {
  width: 100%;
  height: 100vh;
  z-index: 999;
  background-color: rgba(0, 0, 0, 0.5);
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.quiz-modal-wrapper .quiz-modal {
  background-color: white;
  padding: 100px 80px;
  display: flex;
  flex-direction: column;
  border-radius: 20px;
}

.quiz-modal-wrapper .quiz-modal h1 {
  align-self: center;
  text-align: center;
  max-width: 100%;
  text-wrap: wrap;
  color: rgb(94, 158, 255);
}

.quiz-modal-wrapper .quiz-modal p {
  margin-top: 20px;
  align-self: center;
  font-size: 1.2em;
}

.quiz-modal-wrapper .quiz-modal button {
  cursor: pointer;
  color: black;
  background-color: transparent;
  padding: 8px 40px;
  font-size: 1.4em;
  width: fit-content;
  align-self: center;
  border: none;
  margin-top: 20px;
  position: relative;
}

.quiz-modal-wrapper .quiz-modal button:before {
  content: "";
  width: 0;
  background-color: rgb(53, 157, 253);
  right: 0;
  bottom: 100%;
  position: absolute;
  height: 4px;
  transition: 0.3s ease;
}

.quiz-modal-wrapper .quiz-modal button:after {
  content: "";
  width: 0;
  height: 4px;
  background-color: rgb(53, 157, 253);
  left: 0;
  bottom: 0;
  position: absolute;
  transition: 0.3s ease;
}

.quiz-modal-wrapper .quiz-modal button:hover:before,
.quiz-modal-wrapper .quiz-modal button:hover:after {
  width: 20px;
}

.quiz-modal-wrapper .quiz-modal button>.span1 {
  width: 4px;
  height: 0px;
  left: 0;
  bottom: 0;
  position: absolute;
  background-color: rgb(53, 157, 253);
  transition: 0.3s ease;
}

.quiz-modal-wrapper .quiz-modal button>.span2 {
  width: 4px;
  height: 0px;
  right: 0;
  top: 0;
  position: absolute;
  background-color: rgb(53, 157, 253);
  transition: 0.3s ease;
}

.quiz-modal-wrapper .quiz-modal button:hover .span1,
.quiz-modal-wrapper .quiz-modal button:hover .span2 {
  height: 20px;
}

.quiz-modal-wrapper .quiz-modal button.delete-quiz {
  position: absolute;
  bottom: 20px;
  bottom: 40px;
}

.quiz-modal-wrapper .quiz-modal button.delete-quiz:before,
.quiz-modal-wrapper .quiz-modal button.delete-quiz:after,
.quiz-modal-wrapper .quiz-modal button.delete-quiz span {
  background-color: red;
}
</style>