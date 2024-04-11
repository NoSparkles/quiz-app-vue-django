<template>
    <div class="question">
        <h1>{{ question.question }}</h1>
        <ul v-if="!quizEnded">
            <li v-for="(item, index) in question.answers" :key="index"
                :style="{ backgroundColor: index === selectedAnswer ? 'rgb(18, 255, 97)' : '' }"
                @click="handleClick(index)">{{ item }}
            </li>
        </ul>
        <ul v-else>
            <li v-for="(item, index) in question.answers" :key="index" :style="{
                backgroundColor: index === correctAnswers[current] ? 'rgb(18, 255, 97)' : index === selectedAnswer && selectedAnswer !== correctAnswers[current] ? 'red' : ''
            }" @click="
                handleClick(index)">{{ item }}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    setup(props, { emit }) {
        const handleClick = (index) => {
            emit('answer', index)
        }
        return {
            handleClick
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
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 40px;
}

.question ul li {
    background-color: rgb(94, 158, 255);
    flex: 1;
    padding: 10px 20px;
    border-radius: 10px;
    min-width: 40%;
    display: flex;
    justify-content: center;
    font-size: 1.4em;
    color: white;
    cursor: pointer;
}
</style>