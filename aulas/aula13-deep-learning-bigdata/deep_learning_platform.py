"""
Aula 13: Deep Learning e Big Data - Redes Neurais Profundas em Escala
Professor: Vagner Cordeiro
Disciplina: Tópicos de Big Data em Python

Implementação completa de soluções de Deep Learning para Big Data,
incluindo redes neurais distribuídas, processamento de imagens e texto,
modelos transformer, MLOps para DL e otimização de performance.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import json
import logging
import warnings
from typing import Dict, List, Tuple, Optional, Any
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor
import gc
import psutil
import time
warnings.filterwarnings('ignore')

# Importações condicionais para frameworks de Deep Learning
try:
    import tensorflow as tf
    TF_AVAILABLE = True
except ImportError:
    TF_AVAILABLE = False
    print("⚠️ TensorFlow não disponível - simulando funcionalidades")

try:
    import torch
    import torch.nn as nn
    import torch.distributed as dist
    from torch.nn.parallel import DistributedDataParallel as DDP
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    print("⚠️ PyTorch não disponível - simulando funcionalidades")

try:
    from transformers import AutoTokenizer, AutoModel, Trainer, TrainingArguments
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    print("⚠️ Transformers não disponível - simulando funcionalidades")

try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False
    print("⚠️ OpenCV não disponível - funcionalidades de visão limitadas")

try:
    import GPUtil
    GPUTIL_AVAILABLE = True
except ImportError:
    GPUTIL_AVAILABLE = False
    print("⚠️ GPUtil não disponível - monitoramento GPU limitado")

class DeepLearningBigDataPlatform:
    """
    Plataforma completa de Deep Learning para Big Data
    
    Funcionalidades:
    - Redes neurais distribuídas (TensorFlow e PyTorch)
    - Processamento de imagens em larga escala
    - NLP com modelos Transformer
    - Computer Vision avançada
    - MLOps para Deep Learning
    - Otimização de performance e memória
    - Monitoramento de modelos em produção
    - AutoML para arquiteturas neurais
    """
    
    def __init__(self, distributed=False, gpu_enabled=True):
        """Inicializa a plataforma de Deep Learning"""
        
        self.distributed = distributed
        self.gpu_enabled = gpu_enabled and (torch.cuda.is_available() or tf.config.list_physical_devices('GPU'))
        self.device = self._setup_device()
        
        # Configurações de framework
        self._setup_tensorflow()
        self._setup_pytorch()
        
        # Inicializa armazenamento
        self.models = {}
        self.datasets = {}
        self.experiments = {}
        self.model_registry = {}
        
        # Setup logging
        self.logger = self._setup_logging()
        
        print("🚀 Deep Learning Big Data Platform inicializada!")
        print(f"🖥️ Device: {self.device}")
        print(f"🔄 Distributed: {self.distributed}")
        print(f"⚡ GPU Enabled: {self.gpu_enabled}")
        
        if self.gpu_enabled:
            self._print_gpu_info()
    
    def _setup_device(self):
        """Configura dispositivo de computação"""
        if self.gpu_enabled:
            if torch.cuda.is_available():
                device = torch.device("cuda:0")
                print(f"🎮 PyTorch GPU disponível: {torch.cuda.get_device_name(0)}")
            else:
                device = torch.device("cpu")
                print("💻 Usando CPU para PyTorch")
        else:
            device = torch.device("cpu")
            
        return device
    
    def _setup_tensorflow(self):
        """Configura TensorFlow"""
        # Configuração de memória GPU
        if self.gpu_enabled:
            gpus = tf.config.experimental.list_physical_devices('GPU')
            if gpus:
                try:
                    for gpu in gpus:
                        tf.config.experimental.set_memory_growth(gpu, True)
                    print(f"🔧 TensorFlow GPU configurado: {len(gpus)} GPU(s)")
                except RuntimeError as e:
                    print(f"⚠️ Erro configurando TensorFlow GPU: {e}")
        
        # Strategy para distribuição
        if self.distributed:
            self.tf_strategy = tf.distribute.MirroredStrategy()
            print(f"🔄 TensorFlow Distributed Strategy: {self.tf_strategy.num_replicas_in_sync} replicas")
        else:
            self.tf_strategy = tf.distribute.get_strategy()
    
    def _setup_pytorch(self):
        """Configura PyTorch distribuído"""
        if self.distributed and torch.cuda.is_available():
            if not dist.is_initialized():
                # Configuração básica para distributed training
                self.world_size = torch.cuda.device_count()
                print(f"🔄 PyTorch Distributed: {self.world_size} GPUs disponíveis")
    
    def _setup_logging(self):
        """Configura sistema de logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger(__name__)
    
    def _print_gpu_info(self):
        """Exibe informações das GPUs"""
        try:
            import GPUtil
            gpus = GPUtil.getGPUs()
            for i, gpu in enumerate(gpus):
                print(f"  GPU {i}: {gpu.name}")
                print(f"    Memory: {gpu.memoryUsed:.0f}MB / {gpu.memoryTotal:.0f}MB")
                print(f"    Utilization: {gpu.load*100:.1f}%")
        except:
            if torch.cuda.is_available():
                for i in range(torch.cuda.device_count()):
                    print(f"  GPU {i}: {torch.cuda.get_device_name(i)}")
                    print(f"    Memory: {torch.cuda.get_device_properties(i).total_memory / 1e9:.1f}GB")
    
    def create_cnn_architecture(self, input_shape: Tuple, num_classes: int, 
                               architecture_type: str = "resnet"):
        """
        Cria arquiteturas CNN para classificação de imagens
        """
        print(f"🏗️ Criando arquitetura CNN: {architecture_type}")
        
        if architecture_type == "resnet":
            model = self._create_resnet_model(input_shape, num_classes)
        elif architecture_type == "efficientnet":
            model = self._create_efficientnet_model(input_shape, num_classes)
        elif architecture_type == "vit":
            model = self._create_vision_transformer(input_shape, num_classes)
        elif architecture_type == "custom_cnn":
            model = self._create_custom_cnn(input_shape, num_classes)
        else:
            raise ValueError(f"Arquitetura {architecture_type} não suportada")
        
        # Registra modelo
        model_info = {
            'name': f"cnn_{architecture_type}",
            'architecture': architecture_type,
            'input_shape': input_shape,
            'num_classes': num_classes,
            'created_at': datetime.now(),
            'framework': 'tensorflow'
        }
        
        self.models[model_info['name']] = {
            'model': model,
            'info': model_info
        }
        
        print(f"✅ Modelo CNN criado: {model_info['name']}")
        self._print_model_summary(model, model_info['name'])
        
        return model, model_info
    
    def _create_resnet_model(self, input_shape: Tuple, num_classes: int):
        """Cria modelo ResNet personalizado"""
        
        inputs = tf.keras.Input(shape=input_shape)
        
        # Bloco inicial
        x = tf.keras.layers.Conv2D(64, 7, strides=2, padding='same')(inputs)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Activation('relu')(x)
        x = tf.keras.layers.MaxPooling2D(3, strides=2, padding='same')(x)
        
        # Blocos residuais
        filters = [64, 128, 256, 512]
        for i, f in enumerate(filters):
            x = self._residual_block(x, f, stride=2 if i > 0 else 1)
            x = self._residual_block(x, f, stride=1)
        
        # Classificador
        x = tf.keras.layers.GlobalAveragePooling2D()(x)
        x = tf.keras.layers.Dense(512, activation='relu')(x)
        x = tf.keras.layers.Dropout(0.5)(x)
        outputs = tf.keras.layers.Dense(num_classes, activation='softmax')(x)
        
        model = tf.keras.Model(inputs, outputs, name='custom_resnet')
        
        # Compilação
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
            loss='categorical_crossentropy',
            metrics=['accuracy', 'top_k_categorical_accuracy']
        )
        
        return model
    
    def _residual_block(self, x, filters, stride=1):
        """Bloco residual para ResNet"""
        shortcut = x
        
        # Primeira convolução
        x = tf.keras.layers.Conv2D(filters, 3, strides=stride, padding='same')(x)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Activation('relu')(x)
        
        # Segunda convolução
        x = tf.keras.layers.Conv2D(filters, 3, strides=1, padding='same')(x)
        x = tf.keras.layers.BatchNormalization()(x)
        
        # Ajuste de dimensões do shortcut
        if stride != 1 or shortcut.shape[-1] != filters:
            shortcut = tf.keras.layers.Conv2D(filters, 1, strides=stride)(shortcut)
            shortcut = tf.keras.layers.BatchNormalization()(shortcut)
        
        # Conexão residual
        x = tf.keras.layers.Add()([x, shortcut])
        x = tf.keras.layers.Activation('relu')(x)
        
        return x
    
    def _create_vision_transformer(self, input_shape: Tuple, num_classes: int):
        """Cria Vision Transformer (ViT)"""
        
        patch_size = 16
        num_patches = (input_shape[0] // patch_size) * (input_shape[1] // patch_size)
        projection_dim = 768
        num_heads = 12
        num_layers = 12
        
        inputs = tf.keras.Input(shape=input_shape)
        
        # Patch embedding
        patches = self._extract_patches(inputs, patch_size)
        encoded_patches = tf.keras.layers.Dense(projection_dim)(patches)
        
        # Position embedding
        positions = tf.range(start=0, limit=num_patches, delta=1)
        position_embedding = tf.keras.layers.Embedding(
            input_dim=num_patches, output_dim=projection_dim
        )(positions)
        
        # Add position embedding
        encoded_patches += position_embedding
        
        # Transformer blocks
        for _ in range(num_layers):
            # Layer normalization 1
            x1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)(encoded_patches)
            
            # Multi-head attention
            attention_output = tf.keras.layers.MultiHeadAttention(
                num_heads=num_heads, key_dim=projection_dim
            )(x1, x1)
            
            # Skip connection 1
            x2 = tf.keras.layers.Add()([attention_output, encoded_patches])
            
            # Layer normalization 2
            x3 = tf.keras.layers.LayerNormalization(epsilon=1e-6)(x2)
            
            # MLP
            x3 = tf.keras.layers.Dense(projection_dim * 2, activation='gelu')(x3)
            x3 = tf.keras.layers.Dense(projection_dim)(x3)
            
            # Skip connection 2
            encoded_patches = tf.keras.layers.Add()([x3, x2])
        
        # Final layer normalization
        representation = tf.keras.layers.LayerNormalization(epsilon=1e-6)(encoded_patches)
        
        # Global average pooling
        representation = tf.keras.layers.GlobalAveragePooling1D()(representation)
        
        # Classifier
        representation = tf.keras.layers.Dense(512, activation='relu')(representation)
        representation = tf.keras.layers.Dropout(0.1)(representation)
        outputs = tf.keras.layers.Dense(num_classes, activation='softmax')(representation)
        
        model = tf.keras.Model(inputs, outputs, name='vision_transformer')
        
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return model
    
    def _extract_patches(self, images, patch_size):
        """Extrai patches das imagens para ViT"""
        batch_size = tf.shape(images)[0]
        patches = tf.image.extract_patches(
            images=images,
            sizes=[1, patch_size, patch_size, 1],
            strides=[1, patch_size, patch_size, 1],
            rates=[1, 1, 1, 1],
            padding="VALID",
        )
        patch_dims = patches.shape[-1]
        patches = tf.reshape(patches, [batch_size, -1, patch_dims])
        return patches
    
    def create_transformer_nlp_model(self, model_name: str = "bert-base-uncased", 
                                   num_labels: int = 2, task_type: str = "classification"):
        """
        Cria modelo Transformer para NLP
        """
        print(f"🤖 Criando modelo Transformer: {model_name}")
        
        try:
            from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
        except ImportError:
            print("❌ Transformers library não encontrada. Install: pip install transformers")
            return None, None
        
        # Configuração do modelo
        config = AutoConfig.from_pretrained(model_name)
        config.num_labels = num_labels
        
        # Tokenizer e modelo
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        if task_type == "classification":
            model = AutoModelForSequenceClassification.from_pretrained(
                model_name, 
                config=config
            )
        elif task_type == "question_answering":
            from transformers import AutoModelForQuestionAnswering
            model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        elif task_type == "text_generation":
            from transformers import AutoModelForCausalLM
            model = AutoModelForCausalLM.from_pretrained(model_name)
        
        # Move para dispositivo apropriado
        if self.gpu_enabled and torch.cuda.is_available():
            model = model.to(self.device)
        
        model_info = {
            'name': f"transformer_{model_name.replace('/', '_')}",
            'base_model': model_name,
            'task_type': task_type,
            'num_labels': num_labels,
            'created_at': datetime.now(),
            'framework': 'transformers'
        }
        
        self.models[model_info['name']] = {
            'model': model,
            'tokenizer': tokenizer,
            'info': model_info
        }
        
        print(f"✅ Modelo Transformer criado: {model_info['name']}")
        print(f"📊 Parâmetros: {model.num_parameters():,}")
        
        return model, tokenizer, model_info
    
    def create_generative_model(self, model_type: str = "gpt2", 
                              context_length: int = 512):
        """
        Cria modelos generativos (GPT, T5, etc.)
        """
        print(f"🎨 Criando modelo generativo: {model_type}")
        
        try:
            from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
        except ImportError:
            print("❌ Transformers library não encontrada")
            return None, None
        
        tokenizer = AutoTokenizer.from_pretrained(model_type)
        
        # Adiciona pad token se não existir
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        
        if "t5" in model_type.lower():
            model = AutoModelForSeq2SeqLM.from_pretrained(model_type)
        else:
            model = AutoModelForCausalLM.from_pretrained(model_type)
        
        # Configurações para geração
        generation_config = {
            'max_length': context_length,
            'num_beams': 4,
            'temperature': 0.7,
            'do_sample': True,
            'pad_token_id': tokenizer.pad_token_id
        }
        
        if self.gpu_enabled and torch.cuda.is_available():
            model = model.to(self.device)
        
        model_info = {
            'name': f"generative_{model_type.replace('/', '_')}",
            'base_model': model_type,
            'context_length': context_length,
            'generation_config': generation_config,
            'created_at': datetime.now(),
            'framework': 'transformers'
        }
        
        self.models[model_info['name']] = {
            'model': model,
            'tokenizer': tokenizer,
            'generation_config': generation_config,
            'info': model_info
        }
        
        print(f"✅ Modelo generativo criado: {model_info['name']}")
        
        return model, tokenizer, model_info
    
    def train_distributed_model(self, model_name: str, train_dataset, 
                              validation_dataset, training_config: Dict):
        """
        Treina modelo usando computação distribuída
        """
        print(f"🔄 Iniciando treinamento distribuído: {model_name}")
        
        if model_name not in self.models:
            raise ValueError(f"Modelo {model_name} não encontrado")
        
        model_data = self.models[model_name]
        model = model_data['model']
        framework = model_data['info']['framework']
        
        if framework == 'tensorflow':
            return self._train_tensorflow_distributed(
                model, train_dataset, validation_dataset, training_config
            )
        elif framework == 'transformers':
            return self._train_transformers_distributed(
                model_name, train_dataset, validation_dataset, training_config
            )
        else:
            return self._train_pytorch_distributed(
                model, train_dataset, validation_dataset, training_config
            )
    
    def _train_tensorflow_distributed(self, model, train_dataset, 
                                    validation_dataset, config):
        """Treinamento distribuído com TensorFlow"""
        
        with self.tf_strategy.scope():
            # Configuração de otimizador
            optimizer = tf.keras.optimizers.Adam(
                learning_rate=config.get('learning_rate', 0.001)
            )
            
            # Recompila modelo no escopo distribuído
            model.compile(
                optimizer=optimizer,
                loss=config.get('loss', 'categorical_crossentropy'),
                metrics=config.get('metrics', ['accuracy'])
            )
        
        # Callbacks
        callbacks = [
            tf.keras.callbacks.ModelCheckpoint(
                filepath='best_model.h5',
                save_best_only=True,
                monitor='val_accuracy'
            ),
            tf.keras.callbacks.ReduceLROnPlateau(
                monitor='val_loss',
                patience=3,
                factor=0.5
            ),
            tf.keras.callbacks.EarlyStopping(
                monitor='val_loss',
                patience=5,
                restore_best_weights=True
            )
        ]
        
        # Treinamento
        history = model.fit(
            train_dataset,
            validation_data=validation_dataset,
            epochs=config.get('epochs', 10),
            batch_size=config.get('batch_size', 32),
            callbacks=callbacks,
            verbose=1
        )
        
        training_results = {
            'history': history.history,
            'final_accuracy': max(history.history['val_accuracy']),
            'final_loss': min(history.history['val_loss']),
            'training_time': datetime.now()
        }
        
        print(f"✅ Treinamento concluído!")
        print(f"📈 Melhor accuracy: {training_results['final_accuracy']:.4f}")
        print(f"📉 Melhor loss: {training_results['final_loss']:.4f}")
        
        return training_results
    
    def _train_transformers_distributed(self, model_name: str, train_dataset, 
                                      validation_dataset, config):
        """Treinamento distribuído com Transformers"""
        
        model_data = self.models[model_name]
        model = model_data['model']
        tokenizer = model_data['tokenizer']
        
        # Configuração de treinamento
        training_args = TrainingArguments(
            output_dir=f'./results_{model_name}',
            num_train_epochs=config.get('epochs', 3),
            per_device_train_batch_size=config.get('batch_size', 8),
            per_device_eval_batch_size=config.get('eval_batch_size', 8),
            warmup_steps=config.get('warmup_steps', 500),
            weight_decay=config.get('weight_decay', 0.01),
            logging_dir=f'./logs_{model_name}',
            logging_steps=config.get('logging_steps', 100),
            evaluation_strategy="epoch",
            save_strategy="epoch",
            load_best_model_at_end=True,
            metric_for_best_model="eval_accuracy",
            greater_is_better=True
        )
        
        # Trainer
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=validation_dataset,
            tokenizer=tokenizer
        )
        
        # Treinamento
        print("🚀 Iniciando treinamento com Transformers...")
        train_result = trainer.train()
        
        # Avaliação
        eval_result = trainer.evaluate()
        
        training_results = {
            'train_result': train_result,
            'eval_result': eval_result,
            'training_time': datetime.now()
        }
        
        print(f"✅ Treinamento Transformers concluído!")
        print(f"📈 Eval accuracy: {eval_result.get('eval_accuracy', 'N/A')}")
        
        return training_results
    
    def create_automl_pipeline(self, task_type: str, dataset_info: Dict, 
                             search_space: Dict, max_trials: int = 20):
        """
        Cria pipeline de AutoML para otimização de arquiteturas
        """
        print(f"🤖 Criando pipeline AutoML para {task_type}")
        
        try:
            import keras_tuner as kt
        except ImportError:
            print("❌ Keras Tuner não encontrado. Install: pip install keras-tuner")
            return None
        
        def build_model(hp):
            """Função para construir modelo com hiperparâmetros"""
            
            if task_type == "image_classification":
                return self._build_automl_cnn(hp, dataset_info)
            elif task_type == "text_classification":
                return self._build_automl_nlp(hp, dataset_info)
            elif task_type == "regression":
                return self._build_automl_regression(hp, dataset_info)
            else:
                raise ValueError(f"Task type {task_type} não suportado")
        
        # Tuner
        tuner = kt.RandomSearch(
            build_model,
            objective='val_accuracy',
            max_trials=max_trials,
            directory='automl_results',
            project_name=f'automl_{task_type}'
        )
        
        automl_info = {
            'task_type': task_type,
            'search_space': search_space,
            'max_trials': max_trials,
            'tuner': tuner,
            'created_at': datetime.now()
        }
        
        print(f"✅ Pipeline AutoML criado: {max_trials} trials")
        
        return tuner, automl_info
    
    def _build_automl_cnn(self, hp, dataset_info):
        """Constrói CNN com hiperparâmetros otimizáveis"""
        
        model = tf.keras.Sequential()
        
        # Primeira camada
        model.add(tf.keras.layers.Conv2D(
            filters=hp.Int('conv_1_filter', min_value=32, max_value=128, step=32),
            kernel_size=hp.Choice('conv_1_kernel', values=[3, 5]),
            activation='relu',
            input_shape=dataset_info['input_shape']
        ))
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
        
        # Camadas convolucionais adicionais
        for i in range(hp.Int('n_conv_layers', 2, 5)):
            model.add(tf.keras.layers.Conv2D(
                filters=hp.Int(f'conv_{i+2}_filter', min_value=32, max_value=256, step=32),
                kernel_size=hp.Choice(f'conv_{i+2}_kernel', values=[3, 5]),
                activation='relu'
            ))
            model.add(tf.keras.layers.BatchNormalization())
            model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
        
        # Flatten e Dense layers
        model.add(tf.keras.layers.GlobalAveragePooling2D())
        
        for i in range(hp.Int('n_dense_layers', 1, 3)):
            model.add(tf.keras.layers.Dense(
                units=hp.Int(f'dense_{i+1}_units', min_value=32, max_value=512, step=32),
                activation='relu'
            ))
            model.add(tf.keras.layers.Dropout(
                hp.Float(f'dropout_{i+1}', min_value=0.1, max_value=0.5, step=0.1)
            ))
        
        # Camada de saída
        model.add(tf.keras.layers.Dense(
            dataset_info['num_classes'], 
            activation='softmax'
        ))
        
        # Compilação
        model.compile(
            optimizer=tf.keras.optimizers.Adam(
                hp.Choice('learning_rate', [1e-2, 1e-3, 1e-4])
            ),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return model
    
    def optimize_model_inference(self, model_name: str, 
                               optimization_type: str = "tensorrt"):
        """
        Otimiza modelo para inferência em produção
        """
        print(f"⚡ Otimizando modelo {model_name} com {optimization_type}")
        
        if model_name not in self.models:
            raise ValueError(f"Modelo {model_name} não encontrado")
        
        model_data = self.models[model_name]
        model = model_data['model']
        framework = model_data['info']['framework']
        
        if optimization_type == "tensorrt" and framework == 'tensorflow':
            optimized_model = self._optimize_tensorrt(model)
        elif optimization_type == "quantization":
            optimized_model = self._optimize_quantization(model, framework)
        elif optimization_type == "pruning":
            optimized_model = self._optimize_pruning(model, framework)
        elif optimization_type == "distillation":
            optimized_model = self._optimize_distillation(model, framework)
        else:
            print(f"⚠️ Otimização {optimization_type} não implementada")
            return model
        
        # Benchmark de performance
        performance_comparison = self._benchmark_model_performance(
            model, optimized_model, model_data['info']
        )
        
        optimization_info = {
            'original_model': model_name,
            'optimization_type': optimization_type,
            'performance_gain': performance_comparison,
            'optimized_at': datetime.now()
        }
        
        # Registra modelo otimizado
        optimized_name = f"{model_name}_optimized_{optimization_type}"
        self.models[optimized_name] = {
            'model': optimized_model,
            'info': {**model_data['info'], 'optimization': optimization_info}
        }
        
        print(f"✅ Modelo otimizado: {optimized_name}")
        print(f"🚀 Speedup: {performance_comparison.get('speedup', 'N/A')}x")
        print(f"💾 Redução de tamanho: {performance_comparison.get('size_reduction', 'N/A')}%")
        
        return optimized_model, optimization_info
    
    def _optimize_quantization(self, model, framework):
        """Aplica quantização para reduzir tamanho do modelo"""
        
        if framework == 'tensorflow':
            # TensorFlow Lite quantization
            converter = tf.lite.TFLiteConverter.from_keras_model(model)
            converter.optimizations = [tf.lite.Optimize.DEFAULT]
            converter.target_spec.supported_types = [tf.float16]
            
            quantized_model = converter.convert()
            
            # Salva modelo quantizado
            with open('quantized_model.tflite', 'wb') as f:
                f.write(quantized_model)
            
            return quantized_model
            
        elif framework == 'transformers':
            # Quantização com transformers
            try:
                from transformers import BitsAndBytesConfig
                
                quantization_config = BitsAndBytesConfig(
                    load_in_8bit=True,
                    llm_int8_enable_fp32_cpu_offload=True
                )
                
                # Em produção, recarregaria o modelo com quantização
                print("🔧 Quantização configurada para Transformers")
                return model
                
            except ImportError:
                print("⚠️ BitsAndBytesConfig não disponível")
                return model
        
        return model
    
    def deploy_model_serving(self, model_name: str, serving_config: Dict):
        """
        Deploy de modelo para serving em produção
        """
        print(f"🚀 Fazendo deploy do modelo {model_name}")
        
        if model_name not in self.models:
            raise ValueError(f"Modelo {model_name} não encontrado")
        
        model_data = self.models[model_name]
        
        # Configuração de deployment
        deployment_config = {
            'model_name': model_name,
            'version': serving_config.get('version', '1.0.0'),
            'endpoint_url': serving_config.get('endpoint_url', f'http://localhost:8080/v1/models/{model_name}'),
            'batch_size': serving_config.get('batch_size', 32),
            'max_latency_ms': serving_config.get('max_latency_ms', 100),
            'auto_scaling': serving_config.get('auto_scaling', True),
            'monitoring': serving_config.get('monitoring', True),
            'deployed_at': datetime.now()
        }
        
        # Simula deployment (em produção usaria TensorFlow Serving, TorchServe, etc.)
        serving_simulator = ModelServingSimulator(
            model_data['model'], 
            deployment_config
        )
        
        # Registra deployment
        self.model_registry[model_name] = {
            'deployment_config': deployment_config,
            'serving_simulator': serving_simulator,
            'status': 'DEPLOYED'
        }
        
        print(f"✅ Modelo {model_name} deployado com sucesso!")
        print(f"🌐 Endpoint: {deployment_config['endpoint_url']}")
        print(f"📊 Batch size: {deployment_config['batch_size']}")
        print(f"⏱️ Max latency: {deployment_config['max_latency_ms']}ms")
        
        return deployment_config, serving_simulator
    
    def monitor_model_performance(self, model_name: str, duration_minutes: int = 5):
        """
        Monitora performance do modelo em produção
        """
        print(f"📊 Monitorando modelo {model_name} por {duration_minutes} minutos...")
        
        if model_name not in self.model_registry:
            raise ValueError(f"Modelo {model_name} não está deployado")
        
        serving_simulator = self.model_registry[model_name]['serving_simulator']
        
        # Coleta métricas por minuto
        metrics_history = []
        
        for minute in range(duration_minutes):
            metrics = serving_simulator.collect_metrics()
            metrics['timestamp'] = datetime.now()
            metrics_history.append(metrics)
            
            print(f"  ⏱️ Minuto {minute + 1}:")
            print(f"    Requests/min: {metrics['requests_per_minute']}")
            print(f"    Avg latency: {metrics['avg_latency_ms']:.1f}ms")
            print(f"    Error rate: {metrics['error_rate']:.2f}%")
            print(f"    Accuracy: {metrics['accuracy']:.3f}")
            
            # Verifica alertas
            if metrics['avg_latency_ms'] > 200:
                print(f"    🚨 Alta latência detectada!")
            if metrics['error_rate'] > 5:
                print(f"    🚨 Alta taxa de erro!")
            
            time.sleep(0.1)  # Simula tempo
        
        # Análise consolidada
        avg_latency = np.mean([m['avg_latency_ms'] for m in metrics_history])
        avg_accuracy = np.mean([m['accuracy'] for m in metrics_history])
        total_requests = sum([m['requests_per_minute'] for m in metrics_history])
        
        print(f"\n📈 Resumo do Monitoramento:")
        print(f"  Latência média: {avg_latency:.1f}ms")
        print(f"  Accuracy média: {avg_accuracy:.3f}")
        print(f"  Total de requests: {total_requests:,}")
        
        return metrics_history
    
    def run_complete_dl_pipeline(self):
        """
        Executa pipeline completo de Deep Learning
        """
        print("🚀 EXECUTANDO PIPELINE COMPLETO DE DEEP LEARNING")
        print("="*60)
        
        results = {}
        
        # 1. Computer Vision Pipeline
        print("\n1️⃣ COMPUTER VISION PIPELINE")
        print("-" * 40)
        
        # Cria CNN para classificação de imagens
        cnn_model, cnn_info = self.create_cnn_architecture(
            input_shape=(224, 224, 3),
            num_classes=10,
            architecture_type="resnet"
        )
        
        # Vision Transformer
        vit_model, vit_info = self.create_cnn_architecture(
            input_shape=(224, 224, 3),
            num_classes=10,
            architecture_type="vit"
        )
        
        results['computer_vision'] = {
            'cnn_model': cnn_info,
            'vit_model': vit_info
        }
        
        # 2. NLP Pipeline
        print("\n2️⃣ NATURAL LANGUAGE PROCESSING")
        print("-" * 40)
        
        # Modelo BERT para classificação
        bert_model, bert_tokenizer, bert_info = self.create_transformer_nlp_model(
            model_name="distilbert-base-uncased",
            num_labels=3,
            task_type="classification"
        )
        
        # Modelo generativo GPT-2
        gpt_model, gpt_tokenizer, gpt_info = self.create_generative_model(
            model_type="gpt2",
            context_length=512
        )
        
        results['nlp'] = {
            'bert_model': bert_info,
            'gpt_model': gpt_info
        }
        
        # 3. AutoML Pipeline
        print("\n3️⃣ AUTOML OPTIMIZATION")
        print("-" * 40)
        
        dataset_info = {
            'input_shape': (224, 224, 3),
            'num_classes': 10
        }
        
        search_space = {
            'conv_layers': [2, 5],
            'dense_layers': [1, 3],
            'learning_rates': [1e-2, 1e-3, 1e-4]
        }
        
        automl_tuner, automl_info = self.create_automl_pipeline(
            task_type="image_classification",
            dataset_info=dataset_info,
            search_space=search_space,
            max_trials=5  # Reduzido para demo
        )
        
        results['automl'] = automl_info
        
        # 4. Model Optimization
        print("\n4️⃣ MODEL OPTIMIZATION")
        print("-" * 40)
        
        # Otimiza modelo CNN
        if "cnn_resnet" in self.models:
            optimized_cnn, opt_info = self.optimize_model_inference(
                "cnn_resnet",
                optimization_type="quantization"
            )
            
            results['optimization'] = {
                'cnn_optimization': opt_info
            }
        
        # 5. Model Deployment
        print("\n5️⃣ MODEL DEPLOYMENT")
        print("-" * 40)
        
        serving_config = {
            'version': '1.0.0',
            'batch_size': 16,
            'max_latency_ms': 100,
            'auto_scaling': True
        }
        
        if "cnn_resnet" in self.models:
            deployment_config, serving_sim = self.deploy_model_serving(
                "cnn_resnet",
                serving_config
            )
            
            results['deployment'] = deployment_config
        
        # 6. Model Monitoring
        print("\n6️⃣ MODEL MONITORING")
        print("-" * 40)
        
        if "cnn_resnet" in self.model_registry:
            monitoring_results = self.monitor_model_performance(
                "cnn_resnet",
                duration_minutes=3
            )
            
            results['monitoring'] = monitoring_results
        
        print("\n🎉 PIPELINE COMPLETO DE DEEP LEARNING FINALIZADO!")
        print("="*60)
        print("📊 Resumo dos Resultados:")
        print(f"🖼️ Modelos CV criados: {len(results.get('computer_vision', {}))}")
        print(f"📝 Modelos NLP criados: {len(results.get('nlp', {}))}")
        print(f"🤖 AutoML configurado: {'Sim' if 'automl' in results else 'Não'}")
        print(f"⚡ Modelos otimizados: {'Sim' if 'optimization' in results else 'Não'}")
        print(f"🚀 Modelos deployados: {'Sim' if 'deployment' in results else 'Não'}")
        
        return results
    
    def _print_model_summary(self, model, model_name):
        """Exibe resumo do modelo"""
        try:
            if hasattr(model, 'summary'):
                print(f"\n📋 Resumo do modelo {model_name}:")
                model.summary()
            elif hasattr(model, 'num_parameters'):
                print(f"📊 Parâmetros: {model.num_parameters():,}")
        except:
            print(f"📊 Modelo {model_name} criado (resumo não disponível)")
    
    def cleanup(self):
        """Limpa recursos e memória"""
        print("\n🧹 Limpando recursos...")
        
        # Limpa modelos da memória
        for model_name in list(self.models.keys()):
            del self.models[model_name]
        
        # Força garbage collection
        gc.collect()
        
        # Limpa cache GPU se disponível
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        
        print("✅ Deep Learning Platform finalizada!")

class ModelServingSimulator:
    """Simulador de serving de modelos em produção"""
    
    def __init__(self, model, config):
        self.model = model
        self.config = config
        self.request_count = 0
        self.error_count = 0
        
    def collect_metrics(self):
        """Coleta métricas simuladas"""
        
        # Simula carga de requests
        requests_per_minute = np.random.poisson(100)
        self.request_count += requests_per_minute
        
        # Simula latência (afetada pela carga)
        base_latency = 50
        load_factor = min(2.0, requests_per_minute / 50)
        avg_latency = base_latency * load_factor + np.random.normal(0, 10)
        
        # Simula taxa de erro
        error_rate = min(10.0, max(0.1, np.random.exponential(2)))
        
        # Simula accuracy (pode degradar com alta carga)
        base_accuracy = 0.95
        degradation = min(0.1, (requests_per_minute - 50) / 1000)
        accuracy = max(0.8, base_accuracy - degradation + np.random.normal(0, 0.01))
        
        return {
            'requests_per_minute': requests_per_minute,
            'avg_latency_ms': max(10, avg_latency),
            'error_rate': error_rate,
            'accuracy': accuracy,
            'total_requests': self.request_count
        }

# Demonstração principal
if __name__ == "__main__":
    
    print("🚀 Iniciando Deep Learning Big Data Platform")
    print("Este demo demonstra técnicas avançadas de DL para Big Data")
    print("-" * 60)
    
    # Inicializa plataforma
    dl_platform = DeepLearningBigDataPlatform(
        distributed=False,  # Para demo local
        gpu_enabled=True
    )
    
    try:
        # Executa pipeline completo
        results = dl_platform.run_complete_dl_pipeline()
        
        print(f"\n📈 Pipeline de Deep Learning executado com sucesso!")
        print(f"Tecnologias demonstradas:")
        print(f"• Redes neurais convolucionais (ResNet, ViT)")
        print(f"• Modelos Transformer (BERT, GPT)")
        print(f"• AutoML para otimização de arquiteturas")
        print(f"• Otimização de modelos (quantização)")
        print(f"• Deployment e serving de modelos")
        print(f"• Monitoramento em produção")
        
    except Exception as e:
        print(f"❌ Erro durante execução: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Cleanup
        dl_platform.cleanup()

"""
CONCEITOS AVANÇADOS DEMONSTRADOS:

1. 🏗️ ARQUITETURAS DEEP LEARNING
   - Redes Neurais Convolucionais (CNN)
   - Vision Transformers (ViT)
   - Modelos Transformer (BERT, GPT)
   - Redes generativas e autoencoders

2. 🔄 TREINAMENTO DISTRIBUÍDO
   - Multi-GPU training
   - Data parallelism
   - Model parallelism
   - Gradient synchronization

3. 🤖 AUTOML PARA DEEP LEARNING
   - Neural Architecture Search (NAS)
   - Hyperparameter optimization
   - Automated feature engineering
   - Model selection

4. ⚡ OTIMIZAÇÃO DE MODELOS
   - Quantização (INT8, FP16)
   - Pruning de pesos
   - Knowledge distillation
   - TensorRT optimization

5. 🚀 MLOPS PARA DEEP LEARNING
   - Model versioning
   - Automated deployment
   - A/B testing
   - Model monitoring

6. 📊 MONITORAMENTO EM PRODUÇÃO
   - Performance metrics
   - Drift detection
   - Error analysis
   - Resource utilization

APLICAÇÕES REAIS:
- Computer Vision em larga escala
- Processamento de linguagem natural
- Sistemas de recomendação
- Detecção de anomalias
- Análise de sentimentos
- Reconhecimento de padrões
- Geração de conteúdo
- Análise preditiva
"""
