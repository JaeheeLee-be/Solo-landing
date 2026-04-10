# Solo-landing

## 브랜치 전략
- `main` : 최종 배포 브랜치
- `develop` : 통합 브랜치
- `feature/기능명` : 기능 개발
- `fix/버그명` : 버그 수정
- `chore/작업명` : 설정, 환경 작업
- `refactor/내용` : 리팩토링

## 커밋 컨벤션
| 타입 | 설명 |
|------|------|
| feat | 새로운 기능 추가 |
| fix | 버그 수정 |
| chore | 설정, 패키지 등 기타 작업 |
| refactor | 기능 변경 없이 코드 구조 개선 |
| docs | 문서 수정 |
| test | 테스트 코드 |
| style | 코드 포맷팅 |

## PR 규칙
- `feature` → `develop` PR 후 머지
- `develop` → `main` 배포 시 머지