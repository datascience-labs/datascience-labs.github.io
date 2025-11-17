# DSL 페이지 작성 지침

> 최종 업데이트: 2025-10-19

## 1. 목적과 적용 범위
- Data Science Lab Jekyll 사이트(`datascience-labs.github.io`)에 새 페이지·포스트를 추가하거나 수정할 때 따라야 할 기준을 정리했습니다.
- 블로그(`blog/_posts`), 멤버 소개(`team/_posts`), 프로젝트(`projects/`), 논문(`papers/_posts`) 등 주기적으로 갱신되는 콘텐츠를 모두 포함합니다.
- 새 유형의 페이지를 만들 때도 본 지침을 기본으로 삼고, 필요한 경우 예외 사항과 추가 규칙을 본 파일에 갱신해 주세요.
- 공통 마크다운 포맷은 `guide/_posts/2013-10-26-style.md`를 참고하세요. [GitHub 보기](https://github.com/datascience-labs/datascience-labs.github.io/blob/main/guide/_posts/2013-10-26-style.md)

## 2. 공통 작성 원칙
- **인코딩**: 모든 파일을 UTF-8(LF)로 저장합니다. 편집기 기본값이 CP949/CRLF라면 UTF-8·LF로 바꾼 뒤 저장하세요.
- **파일명**: 영문 소문자와 숫자만 사용하고, 공백은 하이픈(`-`)으로 대체합니다.
- **Front matter**: 파일 맨 위에 `---` 블록을 두고 `layout`, `title` 등 필수 메타데이터를 정의합니다. 값이 비어 있으면 항목을 삭제합니다.
- **본문 마크다운**: Kramdown 문법을 기본으로 사용하고, HTML은 꼭 필요할 때만 섞습니다.
- **언어 사용**: 문서 성격에 맞춰 한국어·영어를 구분하고, 혼용 시 섹션별 소제목으로 묶어 가독성을 유지합니다.
- **링크·이미지 경로**: 사이트 내부 자산은 절대 경로(`/images/...`)를 사용하고, 외부 링크는 `https://` 여부와 접근 권한을 확인합니다.

## 3. 유형별 체크리스트와 예시

### 3.1 블로그 글 (`blog/_posts`)
- **파일명 규칙**: `YYYY-MM-DD-slug.md`
- **필수 Front matter**
  ```yaml
  ---
  layout: post
  title: 2025 IEEE CASE 참관기
  author: DSL-Media
  ---
  ```
- **선택 항목**: `description`, `thumb`, `categories`, `tags`, `link`, `authors`
- **본문 팁**: `##` 이하 헤딩으로 섹션을 나누고, 이미지 캡션은 마크다운 구문(`![설명](경로)`)을 우선 사용합니다.
- **이미지 관리**: `/images/blog/` 아래에 저장하고 가로 1200px·용량 1MB 이하로 맞춥니다.
- **예시 참고**: `guide/examples/blog-post-example.md` – [GitHub 보기](https://github.com/datascience-labs/datascience-labs.github.io/blob/main/guide/examples/blog-post-example.md)

### 3.2 멤버 소개 (`team/_posts`)
- **파일명 규칙**: `YYYY-MM-DD-name.md` (합류 예정·졸업생은 `9999` 등 정렬용 연도 사용 가능)
- **필수 Front matter**
  ```yaml
  ---
  layout: member
  title: Jane Doe
  kname: 홍길동
  position: Undergraduate Researcher
  image: /images/team/jane-doe.jpg
  ---
  ```
- **선택 항목**: `handle`, `github`, `scholar`, `linkedin`, `website`, `calendar`, `cv`, `email`, `alumni`
- **본문 팁**: `## Brief introduction`, `## Major awards`, `## Research interests` 등 공통 섹션 제목을 활용해 일관성을 유지합니다.
- **예시 참고**: `guide/examples/member-profile-example.md` – [GitHub 보기](https://github.com/datascience-labs/datascience-labs.github.io/blob/main/guide/examples/member-profile-example.md)

### 3.3 프로젝트 페이지 (`projects/<slug>/index.md`)
- **디렉터리 구조**: `projects/<repo-name>/index.md`
- **필수 Front matter**
  ```yaml
  ---
  layout: project
  title: AnomaliFlow
  project: anomali-flow
  repo: datascience-labs/anomali-flow
  permalink: /:path/:basename:output_ext
  ---
  ```
- **본문 팁**: 개요, 주요 기능, 기술 스택, 실행 방법(`## Features`, `## Run` 등)을 나누고 명령어는 fenced code block(````bash`)으로 표시합니다.
- **이미지 관리**: `/images/projects/`에 저장하고, 다이어그램은 SVG 또는 150DPI 이상의 PNG를 사용합니다.
- **예시 참고**: `guide/examples/project-page-example.md` – [GitHub 보기](https://github.com/datascience-labs/datascience-labs.github.io/blob/main/guide/examples/project-page-example.md)

### 3.4 논문·성과 (`papers/_posts`)
- **파일명 규칙**: `YYYY-MM-DD-short-title.md`
- **필수 Front matter**
  ```yaml
  ---
  layout: paper
  ptype: intjour
  group: knowevo
  title: 논문 제목
  authors: 이름1, 이름2
  year: 2025
  categories: papers
  ---
  ```
- **선택 항목**: `journal`, `ref`, `feature`, `doi`, `pdf`, `supplement`, `github`
- **본문 팁**: `## Abstract`, `## Highlights`, `## Resources` 등 명확한 섹션으로 요약하고, DOI는 `https://doi.org/` 접두사를 확인해 링크합니다.
- **예시 참고**: `guide/examples/paper-entry-example.md` – [GitHub 보기](https://github.com/datascience-labs/datascience-labs.github.io/blob/main/guide/examples/paper-entry-example.md)

### 3.5 기타 페이지
- `guide/`, `calendar/`, `misc/` 등 다른 디렉터리도 위 공통 원칙을 따르고, 기존 파일을 템플릿 삼아 Front matter와 섹션 구조를 맞춥니다.
- 새로운 레이아웃을 만들면 `_layouts`에 HTML을 추가하고, 관련 예시 파일과 함께 본 지침을 갱신하세요.
- **예시 참고**: `guide/_posts/2013-10-27-format.md` – [GitHub 보기](https://github.com/datascience-labs/datascience-labs.github.io/blob/main/guide/_posts/2013-10-27-format.md)

## 4. 이미지와 첨부 자원 관리
- 모든 이미지·PDF는 `images/`, `pdfs/` 등 지정 폴더에 저장합니다. 팀 사진은 `/images/team/`, 블로그 이미지는 `/images/blog/`를 사용합니다.
- 파일명은 `콘텐츠유형-연도-주제.jpg` 등으로 일관되게 정리합니다. 예: `team-2025-jane-doe.jpg`
- 용량이 큰 파일은 압축하거나 해상도를 조정해 페이지 로딩 속도를 유지합니다.
- 외부 스토리지 링크는 “링크가 있는 사람 열람 가능” 권한으로 설정하고 주기적으로 만료 여부를 점검합니다.

## 5. 작성 및 검수 절차
1. **초안 작성**: 해당 디렉터리에 새 파일을 만들고, 유사 문서에서 Front matter/섹션 구조를 복사해 내용을 채웁니다.
2. **자체 검수**: 맞춤법, 링크 동작, 이미지 경로, 메타데이터 누락 여부를 확인합니다.
3. **로컬 빌드**: 아래 명령으로 미리 보기 후 레이아웃·링크를 확인합니다.
   ```bash
   bundle install           # 최초 1회
   bundle exec jekyll serve --livereload
   ```
4. **데이터 동기화**: 프로젝트 메타데이터가 필요하면 `_scripts/update-and-preprocess.rb`를 실행합니다.
5. **PR 준비**: 변경 파일과 이미지를 커밋하고, 변경 이유·주요 내용을 간결하게 정리합니다.

## 6. 제출 전 체크리스트
- Front matter에 필수 항목이 모두 존재하고 빈 값은 삭제했는가?
- 파일 인코딩이 UTF-8이고 한글이 깨지지 않는가?
- 이미지 파일이 올바른 폴더에 있고 경로가 절대 경로(`/images/...`)로 연결되는가?
- `bundle exec jekyll build`가 오류 없이 완료되었는가?
- 작성한 내용이 기존 페이지와 톤·형식 면에서 일관되는가?

필요한 새 규칙이나 예외가 생기면 관련 예시 파일을 함께 추가하고, 변경 일자를 이 문서 상단에 업데이트해 주세요.
