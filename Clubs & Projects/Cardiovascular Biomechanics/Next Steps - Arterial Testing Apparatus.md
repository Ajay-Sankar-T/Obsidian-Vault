---
tags: [research, biomechanics, apparatus-design, task-list]
status: active
---

# Next Steps - Arterial Testing Apparatus

## What the current literature establishes

The two supplied papers give a useful starting point, but not a finished apparatus design.

- [[01 Literature/Amabili et al 2020 - Nonlinear Dynamics of Human Aortas for Material Characterization.pdf|Nonlinear Dynamics of Human Aortas for Material Characterization]] demonstrates a mock circulatory loop for ex-vivo aortic segments. It uses clamped ends, imposed axial prestretch, measured pressures and laser-based diameter tracking. Its pressure-diameter hysteresis supports dynamic stiffness and loss-factor identification.
- [[01 Literature/Amabili et al 2020 - Biomechanical Characterization of a Chronic Type A Dissected Human Aorta.pdf|Biomechanical Characterization of a Chronic Type A Dissected Human Aorta]] reports axial and circumferential uniaxial tests and explicitly identifies the lack of biaxial testing as a limitation. This makes the biaxial rig a distinct, worthwhile second task.

The immediate goal is therefore to translate these ideas into two safe, calibratable rigs with traceable measurements - not to copy dimensions or operating limits from a different laboratory without confirming them.

---

## Task 1 - Radial expansion testing apparatus

### Goal

Measure pressure, external diameter, and temperature of an intact arterial segment while controlled fluid pressure expands its lumen.

\[
\varepsilon_\theta=\frac{D-D_0}{D_0}
\]

where \(D_0\) is the selected reference diameter and \(D\) is the diameter at the applied pressure. Define the reference pressure and axial boundary condition before testing; they materially affect the result.

### First deliverable: a one-page requirements sheet

Before CAD or purchasing, agree with the professor on these values:

| Requirement | Decision needed | Why it matters |
| --- | --- | --- |
| Specimen | species, artery, expected diameter/length, storage protocol | sets fixture, bath, camera field of view and tubing sizes |
| Loading | static ramp, cyclic waveform, target pressure range and rate | selects pump, compliance chamber and sensor bandwidth |
| Axial condition | fixed length, prescribed prestretch, or measured axial force | strongly affects radial response |
| Medium and temperature | saline/PBS/blood analogue; target temperature and tolerance | determines bath, heater, materials and safety |
| Measurements | pressure resolution, diameter resolution, sampling rate, allowed uncertainty | sets sensor, camera, lighting and DAQ requirements |
| Biosafety | tissue source, containment, disinfecting and waste route | constrains the enclosure and operating procedure |

### Architecture to draw next

```text
Reservoir -> pump / pressure regulator -> compliance & air removal -> inlet pressure sensor
  -> proximal fixture == artery in transparent temperature-controlled bath == distal fixture
  -> outlet pressure sensor -> return / relief path -> reservoir

Camera + backlight / calibration target -> diameter measurement
Temperature probe -> DAQ
Pressure + diameter + temperature -> synchronized acquisition software
```

Include a pressure-relief path, a physical pressure limit, and an easy way to remove trapped air. Do not place the only pressure sensor far upstream if tubing dynamics can make it unrepresentative of specimen pressure.

### Design work in order

1. Sketch two mounting concepts: barbed cannulas with ligatures versus low-damage clamp/seal fixtures. Score leakage resistance, tissue damage, ease of mounting, and compatibility with axial prestretch.
2. Choose pressure generation concept after the required waveform is known: syringe pump/actuator for controlled volume ramps; regulated pump plus compliance for pulsatile loading.
3. Define the transparent bath, heater, temperature probe location, and insulation. Keep optics outside the wetted path where possible.
4. Select a diameter method: calibrated side-view camera is the practical baseline; use two orthogonal views only if ovalization matters. Add diffuse backlighting and a scale/calibration target in the specimen plane.
5. Specify pressure transducer range, wet materials, calibration port, and location close to the specimen. Add a second sensor only if inlet-outlet pressure drop is a research variable.
6. Define a single synchronized time base for pressure, diameter, temperature, pump command, and any axial measurement.

### Verification before tissue testing

- Bench-test with a compliant silicone tube of known dimensions.
- Leak-test the entire fluid path and prove pressure-relief operation.
- Calibrate pressure against a traceable reference and camera pixels against a target at the specimen plane.
- Record a repeatability test: same tube, same waveform, at least three mounting cycles.
- Document uncertainty, sampling rate, filter choices, and the exact reference diameter definition.

### Outputs to produce

- `Requirements and risk register.md`
- block diagram and first CAD assembly
- bill of materials with lead times and alternatives
- calibration procedure and test protocol
- data schema: timestamp, pressure, diameter(s), temperature, axial condition, specimen ID, operator, and run ID

---

## Task 2 - Biaxial tensile testing apparatus

### Goal

Measure the force and deformation of a planar arterial specimen loaded independently along its circumferential and longitudinal directions.

The key output is a coupled response, not two disconnected uniaxial curves. Use the axes consistently in every drawing, specimen label, and data file.

### First deliverable: a one-page requirements sheet

| Requirement | Decision needed | Why it matters |
| --- | --- | --- |
| Coupon | specimen size, thickness, marking method, allowable edge damage | sets grip spacing and optical field of view |
| Loading protocol | displacement- or force-control; equibiaxial and non-equibiaxial ratios | determines actuator/control architecture |
| Force range | expected force and target resolution per axis | selects load cells and overload protection |
| Strain measurement | camera/marker tracking resolution and frame rate | determines lens, lighting and software |
| Environment | bath medium, temperature, access for grips and camera | drives chamber and corrosion-resistant design |
| Grip strategy | hooks/rakes, clamps, or sutures | must minimize slip and stress concentration |

### Architecture to draw next

```text
             y+ actuator + load cell
                     |
        x- arm -- grip -- planar specimen -- grip -- x+ arm
                     |
             y- actuator + load cell

Camera normal to specimen + fiducial markers -> deformation field
Bath + heater + temperature probe -> environment control
All four force/displacement channels + image timestamps -> synchronized DAQ
```

### Design work in order

1. Fix the coordinate convention: circumferential = one axis, longitudinal = the perpendicular axis. Put it on the fixture drawing.
2. Compare two grip concepts. For soft tissue, rakes/hooks or suture loops often distribute load more gently than flat clamps, but their suitability must be demonstrated with a slip/damage test.
3. Choose a mechanically stiff frame and four independently controllable axes. Each axis needs known travel, alignment, force capacity, and an end-stop strategy.
4. Place load cells in line with the specimen and design for zeroing under the bath condition. Avoid side loading.
5. Choose optical tracking: a top-view camera with a high-contrast marker pattern is the baseline. Calibrate image scale and correct lens distortion if strains are derived from marker positions.
6. Define control modes and synchronization. Start with quasi-static displacement-controlled tests; add force control only after the basic system is repeatable.

### Verification before tissue testing

- Check frame compliance and arm alignment with a rigid calibration coupon.
- Calibrate every load cell and displacement channel over the intended operating range.
- Test grip slip and local damage on surrogate material before valuable tissue.
- Validate optical strain using a specimen with known imposed displacement.
- Run repeated equibiaxial and unequal-ratio protocols and quantify force/strain repeatability.

### Outputs to produce

- `Requirements and risk register.md`
- grip-concept comparison and selection rationale
- frame/actuator/load-cell CAD assembly
- control and DAQ block diagram
- specimen preparation, preconditioning, and test protocol
- data schema: timestamp, four forces, four actuator positions, temperature, marker coordinates/strain, specimen orientation, thickness, and run ID

---

## Questions for the next professor meeting

1. Which apparatus is the priority and what is the expected first-review date?
2. What tissue/species and specimen dimensions will actually be available?
3. Are the first studies quasi-static only, or must either rig support pulsatile/dynamic loading immediately?
4. What pressure, force, displacement, temperature, and measurement-resolution targets are acceptable?
5. What lab equipment is already available: pump, camera, DAQ, load cells, heaters, machining/3D printing, and biosafety facilities?
6. Is the expected deliverable a concept design, a CAD design with BOM, or a working prototype?

## Recommended first week

1. Confirm the six questions above with the professor.
2. Make one requirements sheet and one block diagram for each task.
3. Inventory available lab hardware and record model numbers/specifications.
4. Produce two fixture/grip concepts per task and review them before committing to CAD.
5. Start a shared BOM with cost, lead time, supplier, and fallback option.

## Source papers in this folder

- Amabili et al. (2020), *Biomechanical characterization of a chronic type A dissected human aorta*, Journal of Biomechanics, 110, 109978.
- Amabili et al. (2020), *Nonlinear Dynamics of Human Aortas for Material Characterization*, Physical Review X, 10, 011015.
