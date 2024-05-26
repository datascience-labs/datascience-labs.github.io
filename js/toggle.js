document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("toggle-button");
    const textArea = document.getElementById("text-area");

    let currentLanguage = "en";

    const texts = {
        en: 'The Data Science Lab at <a class="off" href="http://www.donga.ac.kr/">Dong-A University</a> aims to incorporate a knowledge graph into recommender systems. Our goal is to discover potential paths between users and items by exploring dynamic interlinks within an evolving knowledge graph. We apply various recommendation, analytics, and reasoning techniques to real-time processing of data streams and (quasi-)static datasets in areas such as air quality monitoring, smart energy monitoring, location intelligence, retail tech, carbon-aware-computing, massive online open courses, and more.',
        ko: "동아대학교 데이터 사이언스 연구실는 추천 시스템에 지식 그래프를 도입하는 것을 목표로 하고 있습니다. 우리의 목표는 진화하는 지식 그래프 내에서 동적인 상호 연결을 탐색하여 사용자와 항목 간의 잠재 경로를 발견하는 것입니다. 우리는 다양한 추천, 추론 기법을 실시간 데이터 스트림 처리 및 정적 데이터셋에 적용하여, 대기질 모니터링, 스마트 에너지 모니터링, 위치 정보, 리테일 테크, 탄소지향 컴퓨팅, 대규모 온라인 공개 강좌(MOOC) 등 여러 분야에서 활용하고 있습니다."
    };

    toggleButton.addEventListener("click", function() {
        currentLanguage = currentLanguage === "en" ? "ko" : "en";
        textArea.value = texts[currentLanguage];
        toggleButton.innerText = currentLanguage === "en" ? "Switch to Korean" : "Switch to English";
    });

    // Initialize text area with English text
    textArea.value = texts[currentLanguage];
    toggleButton.innerText = "Switch to Korean";
});