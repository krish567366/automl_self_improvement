import torch  
from diffusers import DDPMScheduler, UNet2DModel  
from torch.utils.data import Dataset  

class DiffusionAugmenter:  
    def __init__(self, model_name="google/ddpm-cifar10"):  
        self.model = UNet2DModel.from_pretrained(model_name)  
        self.noise_scheduler = DDPMScheduler.from_config(model_name)  

    def augment(self, images: torch.Tensor, num_variants=4) -> torch.Tensor:  
        noisy_images = self.noise_scheduler.add_noise(images, torch.randn_like(images), timesteps=100)  
        with torch.no_grad():  
            generated = self.model(noisy_images).sample  
        return torch.cat([images, generated], dim=0)  