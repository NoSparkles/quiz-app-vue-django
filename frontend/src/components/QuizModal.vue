<template>
  <div class="quiz-modal-wrapper" @click.self="$emit('close')">
    <div class="quiz-modal">
      <h1>{{ title }}</h1>
      <p>Number of questions: {{ numOfQuestions }}</p>
      <button @click="$emit('start')">Start</button>
    </div>
  </div>
</template>

<script>
export default {
  props: [
    'title',
    'numOfQuestions'
  ],
  setup() {
    
    return {

    }
  }
}
</script>

<style>
.quiz-modal-wrapper {
  width: 100%;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  position: fixed;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.quiz-modal-wrapper .quiz-modal {
  z-index: 10;
  background-color: white;
  opacity: 1;
  padding: 40px 100px;
  display: flex;
  flex-direction: column;
  border-radius: 20px;
}
.quiz-modal-wrapper .quiz-modal h1 {
  align-self: center;
  text-align: center;
  max-width: 80%;
  text-wrap: wrap;
}
.quiz-modal-wrapper .quiz-modal p {
  margin-top: 20px;
  align-self: center;
  font-size: 1.2em;
} 
.quiz-modal-wrapper .quiz-modal button {
  cursor: pointer;
  color: white;
  background-color: #555;
  padding: 8px 40px;
  font-size: 1.4em;
  width: fit-content;
  align-self: center;
  border: none;
  margin-top: 20px;
  border-radius: 8px;
}
</style>