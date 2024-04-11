<template>
  <div class="home">
    <QuizModal
  v-if="showModal" 
  :title="modalDetails.title" 
  :numOfQuestions="modalDetails.numOfQuestions"
  @close="showModal=false"
  @start="navigateToQuiz"
  />

    <div class="search">
      <input type="text" v-model="search" placeholder="Search">
    </div>
    <div class="quizes-wrapper">
      <ul>
        <li v-for="(item, index) in computedQuizes" :key="index" @click="toggleModal(index)">
          <h1>{{ item.title }}</h1>
          <p>Number of questions: {{ item.numOfQuestions }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { computed, ref } from 'vue'
import QuizModal from '../components/QuizModal.vue'
import router from '@/router'

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


    return {
      search,
      quizes,
      computedQuizes,
      showModal,
      toggleModal,
      modalDetails,
      navigateToQuiz
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
.home .search {
  display: flex;
}
.home .search > input {
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
  box-shadow: 0px 0px 10px 4px rgba(0, 0, 0, 0.2);
  margin: 20px;
  padding: 20px 32px;
  cursor: pointer;
  border-radius: 10px;
}
.home .quizes-wrapper ul li h1 {
  font-size: 2em;
}
.home .quizes-wrapper ul li p {
  font-size: 1em;
  margin-top: 12px;
}


</style>