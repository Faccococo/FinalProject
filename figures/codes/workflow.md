# Head Tracking Workflow

```mermaid
graph TD
  A[Start] --> B[Input RGB Image]
  B --> C[Detect Faces using YuNet]
  C --> D[Extract Key Points]
  D --> E[Store Key Points in Matrix]
  E --> F[3D Key Points from Sample Head Model]
  F --> G[Retrieve Camera Intrinsic Matrix and Distortion Matrix]
  G --> H[Calculate Pose using solvePnP]
  H --> I[Define Face-Frame for Pose]
  I --> J[Input to Kalman Filter]
  J --> K[Apply Kalman Filter]
  K --> L[Track Head Position]
  L --> M[End]
