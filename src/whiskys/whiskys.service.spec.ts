import { Test, TestingModule } from '@nestjs/testing';
import { WhiskysService } from './whiskys.service';

describe('WhiskysService', () => {
  let service: WhiskysService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [WhiskysService],
    }).compile();

    service = module.get<WhiskysService>(WhiskysService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
