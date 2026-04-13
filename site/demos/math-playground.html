<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Protein Lattice Visualizer | NRC</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body { margin: 0; background: #000; color: #fff; font-family: 'Outfit'; overflow: hidden; }
        .ui { position: absolute; top: 2rem; left: 2rem; width: 300px; padding: 2rem; background: rgba(10,10,20,0.8); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; }
        input { width: 100%; background: #000; border: 1px solid #333; color: #fff; padding: 0.8rem; border-radius: 8px; font-family: 'JetBrains Mono'; margin-top: 1rem; }
        .label { font-size: 0.7rem; color: #666; text-transform: uppercase; letter-spacing: 1px; }
        #canvas-container { width: 100vw; height: 100vh; }
    </style>
</head>
<body>
    <div class="ui">
        <div class="label">NRC Protein Lattice Visualizer</div>
        <div style="font-size: 1.2rem; margin-top: 5px; font-weight: 700;">8192D Manifold Mode</div>
        <input type="text" id="seq" value="MQIFVKTLTGKTITLEVEPSDTIENVKAKIQDKEGIPPDQQRLIFAGKQLEDGRTLSDYNIQKESTLHLVLRLRGG">
        <div class="label" style="margin-top: 2rem;">Lattice Anchor Count: <span id="anchors">24388</span></div>
    </div>
    <div id="canvas-container"></div>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.getElementById('canvas-container').appendChild(renderer.domElement);

        camera.position.z = 100;

        const group = new THREE.Group();
        scene.add(group);

        function createLattice() {
            group.clear();
            const len = document.getElementById('seq').value.length;
            const geo = new THREE.BufferGeometry();
            const pos = [];
            const col = [];
            for(let i=0; i<3000; i++) {
                const phi = 1.618033988;
                const angle = i * 137.5 * (Math.PI / 180);
                const r = Math.sqrt(i) * 3;
                pos.push(Math.cos(angle)*r, Math.sin(angle)*r, (i % len) * 5 - (len*2.5));
                const c = new THREE.Color().setHSL((i % len)/len, 1, 0.5);
                col.push(c.r, c.g, c.b);
            }
            geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
            geo.setAttribute('color', new THREE.Float32BufferAttribute(col, 3));
            const mat = new THREE.PointsMaterial({ size: 1.5, vertexColors: true, transparent: true, opacity: 0.6 });
            group.add(new THREE.Points(geo, mat));
        }

        createLattice();
        document.getElementById('seq').oninput = createLattice;

        function animate() {
            requestAnimationFrame(animate);
            group.rotation.y += 0.002;
            group.rotation.x += 0.001;
            renderer.render(scene, camera);
        }
        animate();
    </script>
</body>
</html>
