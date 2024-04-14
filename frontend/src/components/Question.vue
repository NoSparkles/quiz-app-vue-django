<template>
    <div ref="el" class="question">
        <h1>{{ question.question }}</h1>
        <ul v-if="!quizEnded">
            <li class="hover-effect" v-for="(item, index) in question.answers" :key="index" :style="{
                boxShadow: index === selectedAnswer ? '0px 0px 2px 4px rgba(94, 158, 255, 0.4)' : '',
                border: index === selectedAnswer ? '2px solid rgba(94, 158, 255, 1)' : '',
                color: index === selectedAnswer ? 'rgba(94, 158, 255, 1)' : ''
            }" @click="handleClick(index)">{{ item }}
            </li>
        </ul>
        <ul v-else>
            <li v-for=" (item, index) in question.answers" :key="index" :style="{
                color: index === correctAnswers[current] ? 'rgb(18, 255, 97)' : index === selectedAnswer && selectedAnswer !== correctAnswers[current] ? 'rgb(255, 0, 0)' : '',
                border: index === selectedAnswer ? '2px solid rgba(94, 158, 255, 1)' : '',
                boxShadow: index === selectedAnswer ? '0px 0px 2px 4px rgba(94, 158, 255, 0.4)' : '',
            }">{{ item }}
            </li>
        </ul>

    </div>


</template>

<script>
import gsap from 'gsap'
import { ref, watch, onMounted } from 'vue'



export default {
    setup(props, { emit }) {
        const el = ref(null)

        const handleClick = (index) => {
            emit('answer', index)
        }

        onMounted(() => {
            animateComponent()
        })

        watch(() => props.current, () => {
            animateComponent()
        });

        const animateComponent = () => {
            gsap.fromTo(el.value, {
                opacity: 0,
                y: 40,
            }, {
                opacity: 1,
                y: 0,
                duration: 0.2,
            });
        }

        return {
            handleClick,
            el
        }
    },
    props: [
        'question',
        'current',
        'selectedAnswer',
        'quizEnded',
        'correctAnswers'
    ]

}
</script>

<style>
.question {
    border-radius: 20px;
    box-shadow: 0px 0px 10px 0px #999;
    margin-top: 50px;
    padding: 40px;
    width: 60%;
    align-items: center;
    height: 300px;
}

.question h1 {
    margin: auto;
    margin-top: 20px;
    width: fit-content;
}

.question ul {
    list-style: none;
    width: 100%;
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    margin-top: 40px;
}

.question ul li {
    background-color: white;
    flex: 1;
    padding: 10px 20px;
    border-radius: 4px;
    min-width: 40%;
    display: flex;
    justify-content: center;
    font-size: 1.4em;
    color: #444;
    cursor: pointer;
    border: 2px solid rgba(94, 158, 255, 0.5);
    transition: 0.1s ease;
}

.question ul li.hover-effect:hover {
    border: 2px solid rgba(94, 158, 255, 1);
}

.li-transition {
    transition: 0.5s ease;
}
</style>