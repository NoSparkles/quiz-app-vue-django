<template>
  <div class="home">
    <QuizModal v-if="showModal" :title="modalDetails.title" :numOfQuestions="modalDetails.numOfQuestions"
      @close="showModal = false" @start="navigateToQuiz" />


    <div class="create-quiz">
      <RouterLink to="create">Create quiz</RouterLink>
    </div>
    <div class="search">
      <input type="text" v-model="search" placeholder="Search">
    </div>
    <Transition @enter="animateQuizes">
      <div v-if="computedQuizes.length" class="quizes-wrapper">
        <ul ref="ul">
          <li v-for="(item, index) in computedQuizes" :key="index" @click="toggleModal(index)">
            <h1>{{ item.title }}</h1>
            <p>Number of questions: {{ item.numOfQuestions }}</p>
          </li>
        </ul>
      </div>
      <h1 class="no-quizes" v-else>No quizes were found</h1>
    </Transition>

  </div>
</template>

<script>
import { computed, ref } from 'vue'
import QuizModal from '../components/QuizModal.vue'
import router from '@/router'
import gsap from 'gsap'

export default {
  components: {
    QuizModal
  },
  setup() {
    const search = ref('')
    const quizes = ref([
      {
        title: 'math',
        numOfQuestions: 10,
        id: 1
      },
      {
        title: 'literature',
        numOfQuestions: 11,
        id: 2
      },
      {
        title: 'math 2',
        numOfQuestions: 14,
        id: 3
      },
      {
        title: 'science',
        numOfQuestions: 22,
        id: 4
      },
      {
        title: 'physics',
        numOfQuestions: 7,
        id: 5
      },
      {
        title: 'IT',
        numOfQuestions: 15,
        id: 6
      },
      {
        title: 'Vue',
        numOfQuestions: 20,
        id: 7
      },
    ])
    const showModal = ref(false)
    const modalDetails = ref({
      title: '',
      numOfQuestions: 0,
    })

    const computedQuizes = computed(() => {
      return quizes.value.filter(item => item.title.toLowerCase().includes(search.value.toLowerCase()))
    })

    const toggleModal = (index) => {
      modalDetails.value = {
        title: computedQuizes.value[index].title,
        numOfQuestions: computedQuizes.value[index].numOfQuestions,
        id: computedQuizes.value[index].id,
      }
      showModal.value = true
    }

    const navigateToQuiz = () => {
      router.push('quiz/' + modalDetails.value.id)
    }

    const animateQuizes = (el) => {
      gsap.fromTo(el, {
        opacity: 0,
      }, {
        opacity: 1,
        duration: 0.5
      })
    }


    return {
      search,
      quizes,
      computedQuizes,
      showModal,
      toggleModal,
      modalDetails,
      navigateToQuiz,
      animateQuizes,
    }
  }
}
</script>


<style>
p {
  color: #666;
}

.home {
  width: 100%;
}

.home .create-quiz {
  margin-top: 20px;
}

.home .create-quiz>a {
  color: black;
  font-size: 2em;
  align-self: start;
  margin-left: 40px;
  border-radius: 12px;
  position: relative;
  transition: 0.1s ease;
  cursor: pointer;
}

.home .create-quiz>a::after {
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

.home .create-quiz>a:hover::after {
  width: 100%;
}


.home .search {
  display: flex;
}

.home .search>input {
  margin: auto;
  margin-top: 40px;
  width: 400px;
  height: 40px;
  padding: 4px 8px;
  font-size: 1em;
  border: none;
  outline: none;
  border-bottom: 1px solid #aaa;
}

.home .quizes-wrapper {
  margin: auto;
  margin-top: 40px;
}

.home .quizes-wrapper ul {
  list-style-type: none;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  justify-content: center;
  max-width: 80%;
  margin: auto;
}

.home .quizes-wrapper ul li {
  z-index: 0;
  box-shadow: 0px 0px 10px 4px rgba(0, 0, 0, 0.2);
  margin: 20px;
  padding: 20px 32px;
  cursor: pointer;
  border-radius: 10px;
  transition: 0.3s ease;
}

.home .quizes-wrapper ul li:hover {
  box-shadow: 0px 8px 10px 4px rgba(94, 158, 255, 0.2);
  transform: translateY(-4px);
}

.home .quizes-wrapper ul li h1 {
  font-size: 2em;
  color: rgb(94, 158, 255);
}

.home .quizes-wrapper ul li p {
  font-size: 1em;
  margin-top: 12px;
}

.no-quizes {
  text-align: center;
  margin-top: 40px;
}
</style>