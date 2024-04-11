<template>
  <div class="quiz">
    <QuizToast v-if="showToast" @close="showToast = false" />
    <YesNoModal v-if="showSubmitModal" question="Are you sure you want to submit your answers?" yesText="yes"
      noText="no" @yes="handleSubmit" @no="showSubmitModal = false" />
    <RouterLink to="/">HOME</RouterLink>
    <h1>{{ quiz.title }}</h1>
    <Question :question="quiz.questions[currentQuestion]" :current="currentQuestion" @answer="handleAnswer"
      :selectedAnswer="selectedAnswers[currentQuestion]" :quizEnded="quizEnded" :correctAnswers="correctAnswers" />
    <QuestionsNavigation :numOfQuestions="quiz.questions.length" :current="currentQuestion"
      @changeQuestion="changeCurrentQuestion" />
    <button v-if="!quizEnded" class="end-quiz" @click="handleSubmitButtonClick">Submit</button>
    <h2 v-if="quizEnded" class="quiz-score">Your result: {{ numberOfcorrectAnswers }} / {{ quiz.questions.length }}</h2>
  </div>
</template>

<script>
import { computed, ref } from 'vue'
import { useRoute } from 'vue-router';
import Question from '../components/Question.vue'
import QuestionsNavigation from '../components/QuestionsNavigation.vue'
import YesNoModal from '../components/YesNoModal.vue'
import QuizToast from '@/components/QuizToast.vue';


export default {

  components: {
    Question,
    QuestionsNavigation,
    YesNoModal,
    QuizToast
  },
  setup() {
    const route = useRoute()
    const id = route.params.id
    const currentQuestion = ref(0)
    const quiz = ref(
      {
        title: 'Math',
        questions: [
          {
            question: '2 + 2?',
            answers: [
              '3',
              '2',
              '4',
              '5'
            ],
            correct: 2 // index of correct answer
          },
          {
            question: '7 + 14?',
            answers: [
              '33',
              '21',
            ],
            correct: 1 // index of correct answer
          },
          {
            question: '22 + 88?',
            answers: [
              '100',
              '110',
              '2288'
            ],
            correct: 1 // index of correct answer
          },
        ]
      })
    const correctAnswers = computed(() => {
      let res = Array(quiz.value.questions.length)
      quiz.value.questions.map((item, index) => {
        res[index] = item.correct
      })
      return res
    })
    const selectedAnswers = ref(Array(quiz.value.questions.length).fill(null))
    const quizEnded = ref(false)
    const numberOfcorrectAnswers = computed(() => {
      let score = 0
      for (let i = 0; i < selectedAnswers.value.length; i++) {
        if (selectedAnswers.value[i] == quiz.value.questions[i].correct) {
          score++
        }
      }
      return score
    })
    const showSubmitModal = ref(false)
    const showToast = ref(false)

    const changeCurrentQuestion = (index) => {
      currentQuestion.value = index
    }

    const handleAnswer = (answer) => {
      selectedAnswers.value[currentQuestion.value] = answer
    }
    const handleSubmitButtonClick = () => {
      console.log(selectedAnswers.value)
      let allAnswered = true
      for (let i = 0; i < selectedAnswers.value.length; i++) {
        if (selectedAnswers.value[i] === null) {
          allAnswered = false
        }
      }
      if (allAnswered) {
        showSubmitModal.value = true
      }
      else {
        showToast.value = true
      }
    }
    const handleSubmit = () => {
      showSubmitModal.value = false
      quizEnded.value = true
    }

    return {
      id,
      quiz,
      currentQuestion,
      changeCurrentQuestion,
      selectedAnswers,
      handleAnswer,
      quizEnded,
      numberOfcorrectAnswers,
      showSubmitModal,
      handleSubmit,
      correctAnswers,
      handleSubmitButtonClick,
      showToast
    }
  }
}
</script>

<style>
.quiz {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.quiz>a {
  margin-top: 20px;
  font-size: 2em;
  font-weight: bold;
  align-self: start;
  margin-left: 40px;
  border: 4px solid rgb(94, 158, 255);
  padding: 4px 20px;
  border-radius: 12px;
  transition: 0.1s ease;
}

.quiz>a:hover {
  background-color: rgb(94, 158, 255);
  color: white;
}

.quiz>h1 {
  font-size: 3em;
  margin-top: 50px;
}

.quiz .end-quiz {
  position: absolute;
  margin-top: 20px;
  font-size: 2em;
  font-weight: bold;
  align-self: start;
  right: 40px;
  border: 4px solid rgb(94, 158, 255);
  color: rgb(94, 158, 255);
  padding: 4px 20px;
  border-radius: 12px;
  cursor: pointer;
  transition: 0.1s ease;
}

.quiz>.end-quiz:hover {
  background-color: rgb(94, 158, 255);
  color: white;
}

.quiz .quiz-score {
  position: absolute;
  font-size: 2em;
  color: rgb(94, 158, 255);
  border-bottom: 4px solid rgb(94, 158, 255);
  margin-top: 20px;
}
</style>