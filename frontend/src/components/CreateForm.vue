<template>
  <div class="form-wrapper">
    <form @submit.prevent="handleSubmitButton">
      <Toast v-if="showToast" :text="toastText" @close="showToast = false" />
      <YesNoModal v-if="showModal" question="Are you sure you want to create this quiz?" yesText="yes" noText="no"
        @no="() => { showModal = false }" @yes="handleSubmit" />
      <button class="submit">Submit</button>
      <textarea class="title" type="text" v-model="title" placeholder="Title"
        :style="{ border: titleError ? '1px solid red' : '1px solid white' }" />
      <TransitionGroup tag="ul" name="list" class="questions">
        <li v-for="(question, qIndex) in questions" :key="question">
          <div class="remove-question">
            <button type="button" @click="() => removeQuestion(qIndex)">Remove question</button>
          </div>
          <div class="question-wrapper">
            <label :style="{ color: questionsErrors.has(qIndex) ? 'red' : '' }">{{ qIndex + 1
              }}.</label>
            <input type="text" :placeholder="'Question'" v-model="questions[qIndex].body"
              :style="{ borderBottom: questionsErrors.has(qIndex) ? '1px solid red' : '' }">
          </div>

          <TransitionGroup tag="ul" name="list" class="answers">
        <li v-for="(answer, aIndex) in question.answers" :key="answer">
          <label :for="qIndex + '-' + aIndex" class="radio-container" :style="{
            boxShadow: aIndex === question.correct ? '0px 0px 2px 4px rgba(94, 158, 255, 0.4)' : '',
            border: aIndex === question.correct ? '2px solid rgba(94, 158, 255, 0.8)' : correctErrors.has(qIndex) ? '2px solid red' : '',
            color: aIndex === question.correct ? 'rgba(94, 158, 255, 1)' : ''
          }">
            Correct answer
            <input :id="qIndex + '-' + aIndex" type="radio" :value="aIndex" v-model="question.correct" />
          </label>

          <label :style="{ color: answersErrors.has(`${qIndex}-${aIndex}`) ? 'red' : '' }" class="answer-label">{{
            aIndex
            + 1
          }}.</label>
          <input :style="{ borderBottom: answersErrors.has(`${qIndex}-${aIndex}`) ? '1px solid red' : '' }"
            class="answer" type="text" :placeholder="'Answer'" v-model="question.answers[aIndex].body">
          <button type="button" class="remove" @click="() => removeAnswer(qIndex, aIndex)">Remove
            answer</button>
        </li>
      </TransitionGroup>
      <div class="add-answer">
        <button type="button" class="add" @click="() => addAnswer(qIndex)">Add answer</button>
      </div>
      <hr v-if="qIndex !== questions.length - 1">
      </li>
      </TransitionGroup>
      <div class="add-question">
        <button @click="addQuestion" type="button">Add question</button>
      </div>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue'
import YesNoModal from './YesNoModal.vue'
import Toast from './Toast.vue'
import router from '@/router'

export default {
  setup() {
    const title = ref('')
    const questions = ref([
      {
        body: '',
        answers: [
          {
            body: '',
          },
          {
            body: '',
          }
        ],
        correct: undefined
      }
    ])
    const showModal = ref(false)
    const toastText = ref('')
    const showToast = ref(false)
    const titleError = ref(false)
    const questionsErrors = ref(new Set())
    const answersErrors = ref(new Set())
    const correctErrors = ref(new Set())

    const addAnswer = (qIndex) => {
      if (questions.value[qIndex].answers.length == 4) {
        toastText.value = 'Number of answers cannot be more than 4'
        showToast.value = true
        return
      }
      questions.value[qIndex].answers.push({ body: '' })
    }

    const removeAnswer = (qIndex, aIndex) => {
      if (questions.value[qIndex].answers.length === 2) {
        toastText.value = 'Number of answers cannot be less than 2'
        showToast.value = true
        return
      }
      answersErrors.value.clear()
      questions.value[qIndex].answers = questions.value[qIndex].answers.filter((item, i) => {
        return i !== aIndex
      })
    }

    const addQuestion = () => {
      if (questions.value.length == 5) {
        toastText.value = 'Number of questions cannot be more than 5'
        showToast.value = true
        return
      }
      questions.value.push({
        body: '',
        answers: [
          {
            body: '',
          },
          {
            body: '',
          }
        ],
        correct: undefined
      })
    }

    const removeQuestion = (qIndex) => {
      if (questions.value.length == 1) {
        toastText.value = 'Number of questions cannot be less than 1'
        showToast.value = true
        return
      }
      questionsErrors.value.clear()
      answersErrors.value.clear()
      correctErrors.value.clear()
      questions.value = questions.value.filter((item, i) => {
        return i !== qIndex
      })
    }

    const handleSubmitButton = () => {
      let ok = true
      if (title.value.length === 0) {
        ok = false
        titleError.value = true
      }
      else {
        titleError.value = false
      }
      questions.value.map((question, q) => {
        if (question.body === '') {
          ok = false
          questionsErrors.value.add(q)
        }
        else {
          questionsErrors.value.delete(q)
        }
        if (question.correct === null || question.correct === undefined || question.correct >= question.answers.length) {
          correctErrors.value.add(q)
          ok = false
          console.log('correct', q)
        }
        else {
          correctErrors.value.delete(q)
        }
        question.answers.map((answer, a) => {
          if (answer.body === '') {
            ok = false
            answersErrors.value.add(`${q}-${a}`)
          }
          else {
            answersErrors.value.delete(`${q}-${a}`)
          }
        })
      })
      if (ok === false) {
        showToast.value = true
        toastText.value = 'Not all fields are filled.'
      }
      else {
        showModal.value = true
      }
    }

    const handleSubmit = () => {
      showModal.value = false

      const createQuiz = async () => {
        let data = null
        try {
          let res = await fetch('http://127.0.0.1:8000/create/', {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify({ title: title.value, questions: questions.value })
          })
          data = await res.json()
        }
        catch (error) {
          toastText.value = error
          showToast.value = true
        }

        return data
      }

      createQuiz().then(() => router.push('/'))
    }


    return {
      title,
      questions,
      showModal,
      addAnswer,
      removeAnswer,
      toastText,
      showToast,
      addQuestion,
      handleSubmitButton,
      handleSubmit,
      removeQuestion,
      titleError,
      questionsErrors,
      answersErrors,
      correctErrors,
    }
  },
  components: {
    Toast,
    YesNoModal
  }
}
</script>

<style>
.form-wrapper {
  margin-top: 20px;
  margin-bottom: 100px;
}

.form-wrapper form {
  width: 80%;
  margin: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-wrapper form .submit {
  position: absolute;
  margin-top: 0px;
  font-size: 1.4em;
  align-self: start;
  left: 50%;
  transform: translateX(-50%);
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

.form-wrapper form .submit:hover {
  transform: translateX(-50%) translateY(-4px);
  background-color: rgb(94, 158, 255);
  color: white;
  box-shadow: 0px 12px 10px -2px rgba(94, 158, 255, 0.5);

}

.form-wrapper form .title {
  margin-top: 100px;
  padding: 20px 32px;
  border: none;
  outline: none;
  font-size: 2em;
  box-shadow: 0px 0px 10px 2px rgba(0, 0, 0, 0.2);
  width: 100%;
  overflow-y: scroll;
  height: 4em;
  resize: none;
}

.form-wrapper form .questions {
  list-style: none;
  margin-top: 20px;
  box-shadow: 0px 0px 10px 2px rgba(0, 0, 0, 0.2);
  padding: 20px 20px;
  width: 100%;
  flex-direction: column;
  align-items: center;
}

.form-wrapper form .questions li .remove-question {
  display: flex;
  justify-content: start;
  width: 100%;
}

.form-wrapper form .questions li .remove-question button {
  font-size: 1.4em;
  color: red;
  background-color: white;
  border: 2px solid white;
  padding: 12px 20px;
  font-weight: bold;
  margin-right: 20px;
  cursor: pointer;
  transition: 0.2s ease;
}

.form-wrapper form .questions .remove-question button:hover {
  border: 2px solid red;
}

.form-wrapper form .questions>li {
  width: 100%;
  margin: auto;
  margin-top: 40px;
}

.form-wrapper form .questions>li>.question-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
}

.form-wrapper form .questions>li>.question-wrapper>label {
  font-size: 2em;
}

.form-wrapper form .questions>li>.question-wrapper>input {
  border: none;
  font-size: 2em;
  margin-left: 8px;
  outline: none;
  width: 80%;
  padding: 4px 8px;
  border-bottom: 1px solid #666;
}

.form-wrapper form .questions>li>.add-answer {
  display: flex;
  justify-content: center;
  margin-top: 40px;
  gap: 20px;
}

.form-wrapper form .questions>li>.add-answer>button {
  font-size: 1.2em;
  border: none;
  border-radius: 40px;
  padding: 12px 20px;
  box-shadow: 0px 2px 10px -2px rgba(0, 0, 0, 0.5);
  cursor: pointer;
  color: rgb(18, 255, 97);
  transition: 0.3s ease;
}


.form-wrapper form .questions>li>.add-answer>.add:hover {
  transform: translateY(-4px);
  background-color: rgb(18, 255, 97);
  color: white;
  box-shadow: 0px 8px 10px -2px rgba(18, 255, 97, 0.5);
}

.form-wrapper form .questions>li>.buttons>.remove {
  color: rgb(255, 84, 61);
  transition: 0.3s ease;
}

.form-wrapper form .questions>li>.buttons>.remove:hover {
  transform: translateY(-4px);
  background-color: rgb(255, 84, 61);
  color: white;
  box-shadow: 0px 8px 10px -2px rgba(255, 84, 61, 0.5);
}

.form-wrapper form .questions>li hr {
  margin-top: 32px;
}

.form-wrapper form .questions>li>.answers {
  margin-top: 20px;
  flex-direction: column;
  justify-content: start;
  align-items: start;
  gap: 20px;
  position: relative;
}

.form-wrapper form .questions>li>.answers>li {
  margin-top: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.form-wrapper form .questions>li>.answers>li>.radio-container {
  border: 2px solid rgba(94, 158, 255, 0.2);
  padding: 8px 12px;
  font-size: 1.2em;
  border-radius: 4px;
  color: black;
  transition: 0.1s ease;
  cursor: pointer;
}

.form-wrapper form .questions>li>.answers>li>.radio-container:hover {
  border: 2px solid rgba(94, 158, 255, 0.8);
}

.form-wrapper form .questions>li>.answers>li>.radio-container>input {
  display: none;
}

.form-wrapper form .questions>li>.answers>li>.answer-label {
  font-size: 1.4em;
  margin-left: 8px;
}

.form-wrapper form .questions>li>.answers>li>.answer {
  font-size: 1.4em;
  border: none;
  margin-left: 8px;
  outline: none;
  padding: 4px 8px;
  width: 60%;
  border-bottom: 1px solid #666;

}

.form-wrapper form .questions>li>.answers>li>button {
  margin-left: 20px;
  font-size: 1em;
  padding: 12px 20px;
  color: red;
  font-weight: 600;
  cursor: pointer;
  border-radius: 4px;
  border: 2px solid white;
}

.form-wrapper form .questions>li>.answers>li>button:hover {
  background-color: white;
  border: 2px solid red;
}

.form-wrapper form .add-question button {
  font-size: 1.4em;
  padding: 12px 20px;
  border: 1px solid white;
  color: white;
  background-color: rgb(18, 255, 97);
  border-radius: 8px;
  cursor: pointer;
  margin-top: 32px;
  transition: all 0.2s ease;
}

.form-wrapper .add-question button:hover {
  color: rgb(18, 255, 97);
  background-color: white;
  transform: translateY(-4px);
  box-shadow: 0px 0px 10px 2px rgba(18, 255, 97, 0.5);
}
</style>