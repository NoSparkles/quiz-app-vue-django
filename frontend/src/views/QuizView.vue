<template>
  <div v-if="quiz.title" class="quiz">
    <Toast v-if="showToast" text="You have not selected all answers" @close="showToast = false" />
    <YesNoModal v-if="showSubmitModal" question="Are you sure you want to submit your answers?" yesText="yes"
      noText="no" @yes="handleSubmit" @no="showSubmitModal = false" />

    <RouterLink to="/">Home</RouterLink>
    <button v-if="!quizEnded" class="end-quiz" @click="handleSubmitButtonClick">Submit</button>
    <Transition appear name="quiz-score">
      <h2 v-if="quizEnded" class="quiz-score">Your result: {{ numberOfcorrectAnswers }} / {{ quiz.questions.length }}
      </h2>
    </Transition>


    <h1>{{ quiz.title }}</h1>
    <Question :question="quiz.questions[currentQuestion]" :current="currentQuestion" @answer="handleAnswer"
      :selectedAnswer="selectedAnswers[currentQuestion]" :quizEnded="quizEnded" :correctAnswers="correctAnswers" />

    <QuestionsNavigation :numOfQuestions="quiz.questions.length" :current="currentQuestion"
      @changeQuestion="changeCurrentQuestion" />
  </div>
</template>

<script>
import { computed, ref } from 'vue'
import { useRoute } from 'vue-router';
import Question from '../components/Question.vue'
import QuestionsNavigation from '../components/QuestionsNavigation.vue'
import YesNoModal from '../components/YesNoModal.vue'
import Toast from '@/components/Toast.vue';


export default {

  components: {
    Question,
    QuestionsNavigation,
    YesNoModal,
    Toast
  },
  setup() {
    const route = useRoute()
    const id = route.params.id
    const currentQuestion = ref(0)
    const quiz = ref({
      title: undefined,
      questions: []
    })

    const getQuiz = async () => {
      let res = await fetch('http://127.0.0.1:8000/quizes/' + id + '/')
      let data = await res.json()

      return data
    }

    getQuiz().then((data) => {
      quiz.value = data
      console.log(quiz.value)
    })

    const correctAnswers = computed(() => {
      if (quiz) {
        let res = Array(quiz.value.questions.length)
        quiz.value.questions.map((item, index) => {
          res[index] = item.correct
        })
        return res
      }
      return []

    })
    const selectedAnswers = ref(Array(quiz.value.questions.length).fill(null))
    const quizEnded = ref(false)
    const numberOfcorrectAnswers = computed(() => {
      if (!quiz) {
        return 0
      }
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
  color: black;
  font-size: 2em;
  align-self: start;
  margin-left: 40px;
  border-radius: 12px;
  position: relative;
  transition: 0.1s ease;
}

.quiz>a::after {
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

.quiz>a:hover::after {
  width: 100%;
}

.quiz>h1 {
  font-size: 3em;
  margin-top: 50px;
  color: black;
}

.quiz .end-quiz {
  position: absolute;
  margin-top: 20px;
  font-size: 1.4em;
  align-self: start;
  right: 40px;
  color: black;
  background-color: white;
  border-radius: 4px;
  border: none;
  padding: 12px 32px;
  border-radius: 40px;
  cursor: pointer;
  box-shadow: 0px 4px 10px -2px rgba(0, 0, 0, 0.5);
  transition: 0.3s ease;
}

.quiz>.end-quiz:hover {
  transform: translateY(-4px);
  background-color: rgb(94, 158, 255);
  color: white;
  box-shadow: 0px 12px 10px -2px rgba(94, 158, 255, 0.5);

}

.quiz .quiz-score {
  position: absolute;
  font-size: 2em;
  color: white;
  background-color: rgba(94, 158, 255, 1);
  box-shadow: 0px 4px 10px 2px rgba(0, 0, 0, 0.4);
  padding: 10px 40px;
  border-radius: 40px;
  margin-top: 20px;
}

.quiz-score-enter-from {
  opacity: 0;
  transform: translateY(40px);
}

.quiz-score-enter-active {
  transition: 1s ease;
}
</style>