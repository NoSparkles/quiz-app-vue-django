<template>
    <div class="form-wrapper">
        <form @submit.prevent="() => { showModal = true }">
            <YesNoModal v-if="showModal" question="Are you sure you want to create this quiz?" yesText="yes" noText="no"
                @no="() => { showModal = false }" />
            <button class="submit">Submit</button>
            <textarea class="title" type="text" ref="title" placeholder="Title" />
            <ul class="questions">
                <li v-for="(question, qIndex) in questions" :key="qIndex">
                    <div class="question-wrapper">
                        <label>{{ qIndex + 1 }}.</label>
                        <input type="text" :placeholder="'Question'">
                    </div>

                    <ul class="answers">
                        <li v-for="(answer, aIndex) in question.answers" :key="aIndex">
                            <label>{{ aIndex + 1 }}.</label>
                            <input type="text" :placeholder="'Answer'">
                        </li>
                    </ul>
                    <div class="buttons">
                        <button type="button" class="add">Add answer</button>
                        <button type="button" class="remove">Remove answer</button>
                    </div>
                </li>
                <div class="add-question">
                    <button type="button">Add question</button>
                </div>

            </ul>
        </form>
    </div>
</template>

<script>
import { ref } from 'vue'
import YesNoModal from './YesNoModal.vue'
export default {
    setup() {
        const title = ref('')
        const questions = ref([
            {
                question: '',
                answers: [
                    '',
                    ''
                ]
            },
        ])
        const showModal = ref(false)


        return {
            title,
            questions,
            showModal
        }
    },
    components: {
        YesNoModal,
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
    padding: 12px 20px;
    border: none;
    outline: none;
    font-size: 2em;
    box-shadow: 0px 0px 10px 2px rgba(0, 0, 0, 0.2);
    width: 60%;
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
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 40px;
}

.form-wrapper form .questions>li {
    width: 100%;
    margin: auto;
}

.form-wrapper form .questions>li>.question-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;

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

.form-wrapper form .questions>li>.buttons {
    display: flex;
    justify-content: center;
    margin-top: 40px;
    gap: 20px;
}

.form-wrapper form .questions>li>.buttons>button {
    font-size: 1.2em;
    border: none;
    border-radius: 40px;
    padding: 12px 20px;
    box-shadow: 2px 2px 10px 0px rgba(0, 0, 0, 0.5);
    cursor: pointer
}

.form-wrapper form .questions>li>.buttons>.add {
    color: rgb(18, 255, 97);
    transition: 0.3s ease;
}

.form-wrapper form .questions>li>.buttons>.add:hover {
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

.form-wrapper form .questions>li>.answers {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    gap: 20px;
}

.form-wrapper form .questions>li>.answers>li {
    display: flex;
    align-items: center;
    width: 100%;
    margin-left: 16%;
}

.form-wrapper form .questions>li>.answers>li>label {
    font-size: 1.4em;
}

.form-wrapper form .questions>li>.answers>li>input {
    font-size: 1.4em;
    border: none;
    margin-left: 8px;
    outline: none;
    padding: 4px 8px;
    width: 60%;
    border-bottom: 1px solid #666;

}

.form-wrapper form .add-question {}

.form-wrapper form .add-question button {
    font-size: 1.4em;
    padding: 12px 20px;
    border: 1px solid white;
    color: white;
    background-color: rgb(18, 255, 97);
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.form-wrapper form .add-question button:hover {
    color: rgb(18, 255, 97);
    background-color: white;
    transform: translateY(-4px);
    box-shadow: 0px 0px 10px 2px rgba(18, 255, 97, 0.5);
}
</style>