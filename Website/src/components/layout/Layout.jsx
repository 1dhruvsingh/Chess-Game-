import { Box, Container } from '@chakra-ui/react';
import { motion } from 'framer-motion';
import Navbar from './Navbar';
import Header from './Header';
import Footer from './Footer';

const MotionBox = motion(Box);

function Layout({ children }) {
  return (
    <Box>
      <Navbar />
      <MotionBox
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.5 }}
        minH="100vh"
        pt="80px" // Add padding top to account for fixed navbar
        position="relative"
        _before={{
          content: '""',
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundImage: `
            radial-gradient(circle at 25% 25%, rgba(255, 255, 255, 0.05) 1%, transparent 1%),
            radial-gradient(circle at 75% 75%, rgba(255, 255, 255, 0.05) 1%, transparent 1%)
          `,
          backgroundSize: '60px 60px',
          opacity: 0.5,
          zIndex: -1,
        }}
      >
        {/* Chess piece decorative elements */}
        <Box
          position="fixed"
          top="20%"
          left="5%"
          opacity={0.1}
          transform="rotate(-15deg)"
          fontSize="120px"
          zIndex={-1}
        >
          ♞
        </Box>
        <Box
          position="fixed"
          top="60%"
          right="5%"
          opacity={0.1}
          transform="rotate(15deg)"
          fontSize="120px"
          zIndex={-1}
        >
          ♜
        </Box>
        <Box
          position="fixed"
          bottom="10%"
          left="15%"
          opacity={0.1}
          fontSize="120px"
          zIndex={-1}
        >
          ♝
        </Box>
        <Container maxW="1200px" py={8}>
          <Header />
          <Box flex="1" as="main">
            {children}
          </Box>
          <Footer />
        </Container>
      </MotionBox>
    </Box>
  );
}

export default Layout; 