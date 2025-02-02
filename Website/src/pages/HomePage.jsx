import { Box, Heading, VStack, Button, Text, Grid, useColorModeValue } from '@chakra-ui/react';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';

const MotionBox = motion(Box);
const MotionButton = motion(Button);

function HomePage() {
  const navigate = useNavigate();
  const buttonBg = useColorModeValue('blue.500', 'blue.400');

  const container = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: {
        staggerChildren: 0.2
      }
    }
  };

  const item = {
    hidden: { opacity: 0, y: 20 },
    show: { opacity: 1, y: 0 }
  };

  const features = [
    { title: 'Import Game', path: '/import', description: 'Analyze your past games' },
    { title: 'Practice with AI', path: '/practice', description: 'Challenge our AI opponent' },
    { title: 'Analysis', path: '/analysis', description: 'Deep game analysis' },
    { title: 'Leaderboard', path: '/leaderboard', description: 'See top players' }
  ];

  return (
    <MotionBox
      variants={container}
      initial="hidden"
      animate="show"
      px={4}
    >
      <VStack spacing={8} align="center" mb={16}>
        <MotionBox
          variants={item}
          initial={{ scale: 0.5, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <Heading
            size="2xl"
            bgGradient="linear(to-r, blue.400, purple.500)"
            bgClip="text"
            textAlign="center"
            mb={4}
          >
            Welcome to Chess Master
          </Heading>
        </MotionBox>
        
        <MotionBox variants={item}>
          <Text fontSize="xl" textAlign="center" color="gray.300">
            Enhance your chess game with powerful analysis tools and AI practice
          </Text>
        </MotionBox>
      </VStack>

      <Grid
        templateColumns={{ base: "1fr", md: "repeat(2, 1fr)" }}
        gap={8}
        mt={8}
      >
        {features.map((feature) => (
          <MotionButton
            key={feature.path}
            height="200px"
            bg={buttonBg}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            variants={item}
            onClick={() => navigate(feature.path)}
            display="flex"
            flexDirection="column"
            justifyContent="center"
            _hover={{
              bg: 'blue.600',
              transform: 'translateY(-5px)',
              boxShadow: 'xl',
            }}
            transition="all 0.2s"
          >
            <Heading size="lg" mb={2}>{feature.title}</Heading>
            <Text>{feature.description}</Text>
          </MotionButton>
        ))}
      </Grid>
    </MotionBox>
  );
}

export default HomePage; 