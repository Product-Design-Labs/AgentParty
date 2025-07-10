# Device Status Badge Enhancement - Move to Individual Device Line Items

## 🎯 **Issue Overview**

**Priority:** High  
**Type:** Enhancement  
**Assignee:** @Hamad  
**Labels:** `frontend`, `UX improvement`, `real-time`, `device-management`

## 📝 **Description**

The current implementation of the offline badge is not displaying the online status for each individual device. Instead, it is located in a single area, which does not provide a real-time overview of device statuses. This affects user experience, especially when monitoring multiple devices.

**📺 Demo Video:** [Loom Recording](https://www.loom.com/share/963f1690f0274496b75ae08eed2aea11)

## 🔄 **Steps to Reproduce**

1. Load the webpage that displays device statuses
2. Observe the current location of the offline badge
3. Check if the badge reflects the online status of individual devices
4. Note that the badge does not provide real-time updates for each device

## ✅ **Acceptance Criteria**

- [ ] The offline badge should be moved to each individual device line item
- [ ] Each device should send its online status to a predefined topic in JSON format
- [ ] The JSON response should include a timestamp and relevant device information (e.g., IP address)
- [ ] The webpage should display a green light for devices that are online and a spinner while loading statuses
- [ ] Real-time updates should work without page refresh
- [ ] Status indicators should be visually clear and accessible

## 🏗️ **Comprehensive Development Plan**

### Phase 1: Frontend Component Updates (Sprint 1 - Week 1)

#### 1.1 Component Restructuring
- **File:** `components/DeviceList.tsx` or equivalent
- **Task:** Refactor device list to include individual status badges
- **Estimated Time:** 2-3 days

```typescript
// New component structure
interface DeviceStatusBadge {
  deviceId: string;
  isOnline: boolean;
  lastSeen: Date;
  ipAddress?: string;
  isLoading: boolean;
}
```

#### 1.2 Status Badge Component
- **File:** `components/DeviceStatusBadge.tsx`
- **Task:** Create reusable status badge component
- **Features:**
  - Green light for online devices
  - Red/gray indicator for offline devices
  - Loading spinner during status check
  - Tooltip with last seen timestamp and IP
- **Estimated Time:** 1-2 days

#### 1.3 Real-time Updates Integration
- **Task:** Implement WebSocket or Server-Sent Events for real-time updates
- **Technologies:** WebSocket API or EventSource
- **Estimated Time:** 2-3 days

### Phase 2: Backend API Integration (Sprint 1 - Week 2)

#### 2.1 Device Status API Endpoint
- **Endpoint:** `GET /api/devices/{deviceId}/status`
- **Response Format:**
```json
{
  "deviceId": "device-123",
  "isOnline": true,
  "timestamp": "2024-01-15T10:30:00Z",
  "ipAddress": "192.168.1.100",
  "lastHeartbeat": "2024-01-15T10:29:45Z",
  "metadata": {
    "version": "1.2.3",
    "location": "Building A, Floor 2"
  }
}
```

#### 2.2 Batch Status API
- **Endpoint:** `GET /api/devices/status`
- **Purpose:** Get status for multiple devices in single request
- **Estimated Time:** 2 days

#### 2.3 WebSocket/SSE Implementation
- **Endpoint:** `ws://api/devices/status/live` or `GET /api/devices/status/stream`
- **Purpose:** Real-time status updates
- **Estimated Time:** 3 days

### Phase 3: Testing & Optimization (Sprint 2 - Week 1)

#### 3.1 Unit Tests
- Component rendering tests
- Status update logic tests
- WebSocket connection tests
- **Estimated Time:** 2 days

#### 3.2 Integration Tests
- End-to-end device status flow
- Real-time update scenarios
- Error handling (network failures, timeouts)
- **Estimated Time:** 2 days

#### 3.3 Performance Optimization
- Debouncing status updates
- Efficient re-rendering strategies
- Connection pooling for WebSockets
- **Estimated Time:** 1-2 days

### Phase 4: UI/UX Polish (Sprint 2 - Week 2)

#### 4.1 Visual Design
- Consistent color scheme for status indicators
- Smooth animations for status changes
- Responsive design for mobile devices
- **Estimated Time:** 2 days

#### 4.2 Accessibility
- ARIA labels for status indicators
- Keyboard navigation support
- High contrast mode support
- **Estimated Time:** 1 day

#### 4.3 User Feedback
- Loading states and error messages
- Connection status indicators
- Manual refresh capability
- **Estimated Time:** 1 day

## 🚀 **Suggested Downstream Prompts**

### For Frontend Development:
1. **"Create a React component for individual device status badges with TypeScript interfaces"**
   - Include props for device ID, online status, and timestamp
   - Add loading and error states
   - Implement accessible design patterns

2. **"Implement WebSocket connection for real-time device status updates"**
   - Handle connection failures gracefully
   - Add reconnection logic with exponential backoff
   - Implement proper cleanup on component unmount

3. **"Design responsive CSS for device status indicators"**
   - Create green/red status lights with smooth transitions
   - Add loading spinner animations
   - Ensure mobile-friendly touch targets

### For Backend Integration:
4. **"Create API service class for device status operations"**
   - Implement HTTP client with proper error handling
   - Add retry logic for failed requests
   - Include proper TypeScript types for API responses

5. **"Implement state management for device status data"**
   - Use Redux/Zustand for global status state
   - Add caching strategies for performance
   - Handle optimistic updates

### For Testing:
6. **"Write comprehensive test suite for device status components"**
   - Mock WebSocket connections
   - Test loading and error states
   - Add visual regression tests

7. **"Create E2E tests for real-time status updates"**
   - Simulate device going online/offline
   - Test WebSocket reconnection scenarios
   - Verify UI updates correctly

### For Performance:
8. **"Optimize rendering performance for large device lists"**
   - Implement virtualization for 100+ devices
   - Add memoization for status components
   - Optimize WebSocket message handling

## 📋 **Technical Requirements**

### Frontend Stack
- React 18+ with TypeScript
- State Management: Redux Toolkit or Zustand
- WebSocket: native WebSocket API or socket.io-client
- Styling: CSS Modules or styled-components
- Testing: Jest + React Testing Library

### API Specifications
- RESTful endpoints for initial status
- WebSocket for real-time updates
- JSON response format with timestamps
- Error handling with proper HTTP status codes

### Performance Targets
- Initial load: < 2 seconds for up to 50 devices
- Real-time updates: < 500ms latency
- Memory usage: < 50MB for 100 devices
- Network: Minimize bandwidth with delta updates

## 🔄 **Related Issues/PRs**

- [ ] Backend API development (to be created)
- [ ] WebSocket infrastructure setup (to be created)
- [ ] Design system updates for status indicators (to be created)

## 📈 **Success Metrics**

- [ ] 100% of devices show individual status badges
- [ ] Real-time updates work within 500ms
- [ ] Zero false positive/negative status reports
- [ ] User satisfaction score improvement (post-implementation survey)
- [ ] Reduced support tickets related to device status confusion

## 🎯 **Definition of Done**

- [ ] All acceptance criteria met
- [ ] Code review completed
- [ ] Unit tests passing (>90% coverage)
- [ ] Integration tests passing
- [ ] Performance benchmarks met
- [ ] Accessibility audit passed
- [ ] Documentation updated
- [ ] QA testing completed
- [ ] Stakeholder approval received

---

**Estimated Total Development Time:** 3-4 weeks  
**Sprint Planning:** 2 sprints of 2 weeks each  
**Team Size:** 2-3 developers (1 frontend lead, 1 backend developer, 1 QA engineer)