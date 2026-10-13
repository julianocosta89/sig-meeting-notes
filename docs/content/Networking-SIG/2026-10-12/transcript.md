SIG: Networking SIG
Date: 2026-10-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Antonio Martinez (Cisco Systems, Inc.)** 01:12 And then…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:13 Sorry, Antonio.
**Antonio Martinez (Cisco Systems, Inc.)** 01:15 How you doing?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:17 Good, here.
**Antonio Martinez (Cisco Systems, Inc.)** 01:19 Yeah, good, it's going well.
I think… I think today's gonna be a more… Free… no meeting, because, like, Brighton is out, as a bank also, so I just joined in case someone…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:33 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 01:33 Do you have any topic? What about you? Do you have any topic for today or?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:38 No, did you see the message about the the 64 bit suggestion?
**Antonio Martinez (Cisco Systems, Inc.)** 01:45 And you put it on Slack, right? That was?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:47 So, yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 01:50 I didn't. I didn't look into that one.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:53 It's probably more for Rob. I think Rob was the one with the concern around the large integers.
**Antonio Martinez (Cisco Systems, Inc.)** 02:00 Yeah.
Let me… Let me add that to the next.
Agenda, sure.
Sorry.
Oh, there are more people joining, that's great.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 02:16 Hello, Mohammed.
**Antonio Martinez (Cisco Systems, Inc.)** 02:24 And the concern was about support.
64 int, right?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 02:30 It was the unsigned 64-bit Int.
Yeah.
I can, I can update the notes.
**Antonio Martinez (Cisco Systems, Inc.)** 02:39 Awesome.
And there he goes.
Today, maybe.
A little bit of context, but yeah.
We've done discussion for the next one.
Hey Mohammed, we were mentioning that today a majority of the people in US and Canada are off.
So they they are not joining today. But I still join in case there are any topic. Do you have any topic for today?
Okay.
So in my end, there is not.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 03:26 So… I'll just leave this for next week, then.
Awesome. Oh.
I might… I might not be able to… oh, no, yeah, I can do next week. Yeah, next week's okay.
Are you going to… KubeCon, I was just looking through the last… last week notes.
**Antonio Martinez (Cisco Systems, Inc.)** 03:44 Yeah, yeah, we, we, I am going. What about you? Do you have a chance?
No, it is.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 03:49 So I will be there. And the Maintainer Summit, are you going to be there as well?
**Antonio Martinez (Cisco Systems, Inc.)** 03:54 Yeah, I will be there too.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 03:56 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 03:57 Any… are you gonna speak or something?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 03:59 No. So I was gonna add a… So I got an award from SIG instrumentation.
for the Kubernetes mixing.
Donation.
So.
There's like an award ceremony on the the Maintainer Summit. The last Last thing on the day on the Sunday.
And they invited me to come and receive it in person. So I'll be there. And then I'll be working.
**Antonio Martinez (Cisco Systems, Inc.)** 04:26 account.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 04:27 I'll be working on the Grafana booth in a bit.
**Antonio Martinez (Cisco Systems, Inc.)** 04:29 Nick.
That's pretty cool, man. Awesome. I will be there for sure. I will, I will go over. See you.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 04:36 Oh, yeah. I see you there. So is there going to be… Let's see, I mentioned about a SIG meeting here. Was there anything else been… are we just going to see closer to the time, or informally try and meet up?
**Antonio Martinez (Cisco Systems, Inc.)** 04:50 Yeah, the goal… the goal is, like, the same… I mean, you have been in the past. Yeah. So you know how it works. So they usually put in an agenda with different SIG groups, and then just people pass by.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 05:02 On the October 1st.
**Antonio Martinez (Cisco Systems, Inc.)** 05:04 Usually it is on the OTL exploratory, I think it's called, but last year it wasn't there. So if.
they have this year, it will be there. If not, it will be on the… pavilion in the pavilion. There is usually like a small stone. So yeah, we can do that. But the goal is like Brighton is gonna take a a slot of half an hour, so people might join there in person. We can at least find out one hour to meet in person, everyone.
If not, it will be a little bit ad hoc.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 05:33 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 05:34 That's the idea.
For me, there is no, like, specific topic to discuss, it's more, like, to meet in person, to talk about the roadmap, in my opinion, kind of those things.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 05:44 Okay, sounds good.
Awesome. So, in the meantime.
You got anything in particular that's blocking you that I could look at or help out?
**Antonio Martinez (Cisco Systems, Inc.)** 05:56 Oh, yeah, that's really good, honestly. We have 3 pull requests that needs review, so those 3 are still there. Yeah. So if you can… Use some of your time to review them, probably, but that will be quite welcome, honestly.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 06:11 Sure, okay.
**Antonio Martinez (Cisco Systems, Inc.)** 06:12 And then those are talks for next, how is it called for next week? But the Snmp receiver lost maintainability.
So Sabena and I are going to be code owner. Feel free also in case you want to be code owner, because that's something that not maintained. So the more people who are interested, the better.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 06:36 That's it, yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 06:38 And then, there was one of the… issues that are still open, that have a lot of attraction in terms of a lot of comments. Interest. Honestly.
And then I created a pull request, actually created three to make it simpler to support it. I don't know how familiar you are with SNMP, but SNMP is mainly focused on pulling metrics from devices, but there is also another thing called… Traps. Traps are, like, notification from the device outside, so we just need to listen on our specific port on UDP, and then we can receive those traps, and they are converting to logs. So yeah, this is what I'm gonna support. I mean, I created a pull request to support that, so feel free to take a… First, first look into to that Github issue. There is 3 pull requests. I mean, I try to make it then simple.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:35 Okay, so the issue, is it linked in the notes? 3, 2, oh, this one, yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 07:41 Yeah, is that the one?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:42 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 07:45 So… the main goal is, like, I just wanted to make.
noise in the network group that we are now owning the Snmp receiver. So we can Decide about the roadmap, also, of that component.
And then there was that really cool issue that we can also start supporting. So if you have any feedback, really, really happy to apply and improve it there.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 08:12 Yeah, sure.
Okay.
And these… R3, are they in addition to… yeah, they're set… they're different to the other ones, right?
**Antonio Martinez (Cisco Systems, Inc.)** 08:22 Correct, they are totally… I split it in three. The reason why is because today, existing SNMP receiver is quite focusing on pooling, and now I… my idea, at least, like, we can create a SNMP receiver for pooling.
Drops.
And also for both. So I split a little bit the configuration. And this is the supporting of the SNMP traps, honestly. And then I created a really simple pull request for using a SNMP simulator. I don't have at home a switch or a router.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 08:57 I was gonna ask about that.
So far for testing verification.
**Antonio Martinez (Cisco Systems, Inc.)** 09:00 For testing, it's really cool that… that pull request, honestly, it's… Non-mandatory to be merged, honestly. But yeah, I think it's a good way to put in the inner readme how you can test it out.
your collector, and even if you are contributing, how you can test an LADD, but we can… improved that a lot. That was, like, a starting point of having, like, a A simulator, honestly.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 09:22 Great, okay.
**Antonio Martinez (Cisco Systems, Inc.)** 09:23 question.
So yeah, that's and then also in other things that's not related to me or directly. But explanting, I I might, you know, Antoine, they are creating that Gemini receiver.
It's like the… in case you are not that familiar with Gemini, it's like the next version of SNMP, so… Okay. Network… devices, telemetry data is always pulling, but by pulling, you might lose, like, imagine you're pulling every minute, or every 20 seconds, or whatever, you might lose data.
And then it's a lot of requests also, it's a lot of ways of CPU. So the devices, like Meraki, Fisco, Arista, Juniper, they put together that standard for Gemini. Feel free to read about it, it might be here also. Gemini is, like, network telemetry data could be pushed.
to the… to anywhere, and then if you are receiving those, you can convert them into OpenTelemetry. So it's quite similar to to SNMP in the sense, like, we are creating metrics out of data from the device, but now here is in a push approach, and using that technology is like a…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 10:38 Okay.
**Antonio Martinez (Cisco Systems, Inc.)** 10:38 gRPC Network Management Interface is the chronomole. So, I just put it on the radar, because they are donating that. I said that I'm happy to help, but Antoine already started creating the components and so on, so in case you want to keep an eye on that, it will be a good idea.
Great. I I will do too.
So that's the career state.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 11:01 Okay, cool.
**Antonio Martinez (Cisco Systems, Inc.)** 11:03 On my side.
Awesome.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 11:08 Alright, I might try and have a look at the, the Prometheus exporter as well, the SNMP Prometheus exporter.
**Antonio Martinez (Cisco Systems, Inc.)** 11:15 This.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 11:16 traffic.
**Antonio Martinez (Cisco Systems, Inc.)** 11:16 Next quarter, yeah, they do have one.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 11:18 So, because I spoke to one of the maintainers about trying to, you know, get some collaboration between the AOTEL and Prometheus side, because it's difficult to find the.
Maintain this REST in MP.
Yeah. But they're… they are, like, fully allocated at the moment. They're, like, swamped, basically.
So, so I wonder if, I'll try… I'll try and become familiar with both sides and see if there's any way we can… we can reuse code, because There was, there was a talk at PromCon last week about Yes.
reusing Prometheus exporters inside, openTelemetry receivers as, like, a library.
**Antonio Martinez (Cisco Systems, Inc.)** 12:02 So.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 12:03 So that you don't have to, you know, just keep maintaining them in two different places.
And even there's a way how you can effectively they're looking into how you can take the same code.
But output it in two different ways, you know, one with the semantic conventions of OTLP.
And then another just with the standard, you know, Prometheus metrics export.
**Antonio Martinez (Cisco Systems, Inc.)** 12:26 But.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 12:26 effectively have the same underlying collector code.
So, especially if there's a lack of maintainers on the hotel side.
It'd be interesting to try and, if possible, get merge some of that code.
**Antonio Martinez (Cisco Systems, Inc.)** 12:42 Yeah, yeah, I'm happy to go in that direction also. I saw something also in the SNMP exporter that I really like it. You guys, I don't know what it is now. I created like… Give me a second.
I think it's that one. So you guys have under Prometheus, SNMP. This is like a profile.
And why this useful is because.
If I get back to SNMP, there is one problem that we, OpenTelemetry SNMP receiver didn't solve it yet, is… Today, we are using… I mean, the problem is, like, each device are putting their… their metrics in a different way. That's one of the main problems that today we have.
Okay. I go to a synthetic receiver.
Mmm.
Yeah, and then everything is solved by OID. So, OID identify a metric. So, what I'm trying to mention to you here is, like, Prometheus have solved that by creating a profile, where that OID is that metric name on that device.
So, we don't have that in OpenTelemetry, we are absolutely… customers have to put their own, they have to do their own mapping.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 14:13 Okay.
**Antonio Martinez (Cisco Systems, Inc.)** 14:13 a really cool feature that we can add in the future to the receiver. I know that Prometheus.
have some profiling, but it's far from half all. I know Kentik, which is another company, have also a lot of them. Let me show you, because I was doing that exploration before.
Yeah, I see.
So they also have a lot of profiles here.
like the the huge list. So the the call would be like somehow to combines The most use on under a single repo I wish to have honestly not on there are.
company. Antique is a network company like Juniper or Arisa, or whatever. So honestly, it could be great to have it under standard like Prometheus. I like the idea. We can keep reusing that one in case it is some have some attraction already. But yeah, it is like we should have that mapping.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 15:10 Okay, so are these like the… are these like the MIBs?
these programs.
**Antonio Martinez (Cisco Systems, Inc.)** 15:14 Yeah, yeah, yeah, yeah, this is what I'm talking. Yeah.
They do the mapping from there, or… OID to the actual metric name, yeah, based on the device.
Let me see if I can show you an example.
Yeah, this is what I meant. This is the OID, and this is the name, and they put some sort of how much they're pulling, which stack they have.
And even they put, like, the annual and so on. That's mapping.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 15:44 Okay.
**Antonio Martinez (Cisco Systems, Inc.)** 15:44 Customer have in open telemetry, they have to write themselves.
It's, it's not, predefined is what I mean.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 15:52 Right.
So yeah, so if you're using the Otel SNMP receiver for every device, you have to specify the full Macro as well. Okay.
**Antonio Martinez (Cisco Systems, Inc.)** 15:59 But most likely with LLMs, it's not the end of the world.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 16:02 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 16:03 We have a predefined, it could be like an important improvement.
So yeah, that could be, like, next… one of the main… project of this product, of that component, I would say.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 16:14 Okay, so in the simulator, does it have, like, a few… Like MIB's already specified, does it pretend to be, like, a certain device, or is it… Is it not? Is it doing something like that?
**Antonio Martinez (Cisco Systems, Inc.)** 16:26 I didn't explore it on that yet, but.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 16:29 I'm.
**Antonio Martinez (Cisco Systems, Inc.)** 16:29 More likely that's quite flexible on that sense.
I might… Because I was using… using that SFTP.
Yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 17:18 You must have some predefined.
**Antonio Martinez (Cisco Systems, Inc.)** 17:21 You could build SNMP from a M file. So yeah, most likely we can use something probably like, I don't know, like from.
For any specific device, we can build order metrics.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 17:35 Okay.
**Antonio Martinez (Cisco Systems, Inc.)** 17:36 But yeah, it's need more, more reading, at least from my side. Yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 17:40 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 17:41 I have to admit.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 17:43 Okay.
**Antonio Martinez (Cisco Systems, Inc.)** 17:44 Awesome, but yeah, I just wanted to share with you something that I found interesting.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 17:48 Correct?
**Antonio Martinez (Cisco Systems, Inc.)** 17:52 Cool. So… I think. Mohammed, are you still there?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 18:04 Maybe they have a mic.
issues.
**Antonio Martinez (Cisco Systems, Inc.)** 18:08 Okay, so… Talk to you next Monday if everything's right on. Yeah, welcome any feedback.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 18:15 Cool, great.
Thank you.
**Antonio Martinez (Cisco Systems, Inc.)** 18:18 Everyone see me?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 18:19 Bye.
