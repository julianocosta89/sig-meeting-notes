SIG: FAAS WG
Date: 2025-10-23
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Tyler Benson** 02:56 Howdy hello, everyone!
**Warre Pessers** 03:01 Hello?
**Tyler Benson** 03:02 Not really sure why we've got this, AI bot in here.
**Warre Pessers** 03:09 Did you do this, or how did you get in?
**Tyler Benson** 03:11 What do we look?
Gotta see what we can do to get rid of it, but yeah, it's not me.
**Warre Pessers** 03:36 Seems like there's no way to, like, kick it from the meeting.
Or at least I'm not able to.
**Tyler Benson** 03:43 Yeah.
**Serkan Özal** 05:05 Okay, shall we start, guys?
**Warre Pessers** 05:11 But yeah, looks like no one else is coming, today, so… Yeah.
**Serkan Özal** 05:20 Any specific topic to discuss?
I don't have, actually.
**Warre Pessers** 05:27 Me neither, I just…
like, the message I sent in the back channel, chat. There's some stuff I need to, open a PR for the…
on the semantic conventions, to, like, change the Lambda SQS spec, because there's some stuff in there that if we have to adhere to that, we can't possibly properly…
Implement the, context propagation, but…
Yeah, I'm working with, the people on the SEMConf,
project for that, so… finally, I, I'm…
Getting a little bit more free time as well, so… hope to get this pushed through, like, in the next week.
**Tyler Benson** 06:18 Okay, I got rid of the bot.
**Serkan Özal** 06:20 Sound good.
**Warre Pessers** 06:21 Nice.
And then that's it for me. I've got nothing else for today.
**Serkan Özal** 06:33 Okay, from my end, there's no, I mean, activity. I was just looking into the Service Express, instrumentation issue by Alessandro.
And also, while passing through the issues in the GitHub, I have seen that, actually, some of them has already been closed, but there were some issues, and the question about how
can use their own custom instrumentation packages. Like, for example, an example is the Prisma, for example. Prisma is not…
out of the box, supported by the OpenTelemetry as instrumentation packages, but they have their own third-party instrumentation packages, so people are… how should people, add those third-party instrumentation packages into their own Lambda functions without
building and releasing their own layers. Currently, there's a workaround about the… the create instrumentation functions over the global object, but it requires, I mean, many steps and,
I think we might think… for such cases, not just the custom instrumentation packages, but for some… for such cases, like, which requires, customizations over the global function.
We might think of providing better and easier way for the users, but at the moment, I don't have any strong opinion to address that, but…
Yeah, that's the thing what I'm thinking of.
**Tyler Benson** 08:13 Okay, I just updated the new section for the meeting notes. If both of you could add, kind of, what you're discussing in the meeting notes, so that we can have a record of that.
I, I got distracted and wasn't taking notes, I apologize.
**Warre Pessers** 08:30 No worries, I'll, add my, points.
**Serkan Özal** 08:35 Okay, if there's no question?
I think we can leave early?
**Warre Pessers** 08:43 No, yeah, I'll… I'll look at that issue you just talked about, just to see if I understand, but, sounds reasonable, what you said.
**Tyler Benson** 09:01 So I always forget, just for future reference, what languages are both of you the most familiar or expert with?
Python, Node.js?
**Serkan Özal** 09:17 Actually, I mean, I am Java and Node.js, but I also have experience with Python too, because, I mean, we were… I mean, years ago, we were building a serverless monitoring solution, so I had to deal with Python too, but…
I am, I mean, more experienced with Java and Node.js.
**Tyler Benson** 09:35 Okay.
What about you, Rory?
**Warre Pessers** 09:38 Yeah, mostly Java and, also Node.js, but, currently, due to what we're doing at work, Python is becoming a little bit more relevant for me as well.
So mostly those. I have some very limited experience with Rust, but we don't even have a layer for Rust lambdas, I don't think, so that's not really relevant here.
**Tyler Benson** 10:04 Okay, yeah, I didn't realize both of you already had good Java experience, so that's… that's cool. I'm primarily just Java. I've dabbled in Node.js a long time ago, but that area moves so fast that I haven't been able to keep up, so I'm…
Pretty much primarily Java.
**Warre Pessers** 10:26 Okay, cool. Yeah, I saw you, like, did a bunch of work on the instrumentation,
for Java instrumentation packages.
**Serkan Özal** 10:36 Yeah.
Yeah, I know Tyler from the Datadog, I mean, you are…
I think it's first time you were leading the Datadoc Java agent, right?
**Tyler Benson** 10:44 Yeah, I was their first, Java agent developer, back in the day.
So, I founded that team, which eventually got donated to OpenTelemetry for the Java agent.
So, I'm not the primary contributor anymore, but if you look in, like, the, the…
The contributor stats for the instrumentation, Java agent, I'm still pretty high up there.
**Serkan Özal** 11:14 Yeah.
Cool.
What'd jump?
**Tyler Benson** 11:19 Thanks.
Anyway, yeah, I… I don't have anything specific to talk about,
I appreciate both of you continuing to work on this. I just don't have as much time as I used to anymore, given the shift in my work focus, so…
I'm mainly just trying to stay here and keep the lights on, so to speak.
**Warre Pessers** 11:48 Yeah, totally understand that. I'm also trying to do my best. Sometimes I have some busier periods at work, sometimes not so much, and then I can do a lot of stuff here, but, like, not consistently, so I try.
**Tyler Benson** 12:04 Yep.
Great, well, have a great day, both of you.
We'll see you in a couple weeks, and, on Slack.
**Warre Pessers** 12:14 Yeah, sure, I'll keep you posted on, like, the, spec changes I talked about.
Great.
**Tyler Benson** 12:20 Appreciate it.
**Warre Pessers** 12:21 Alright.
**Serkan Özal** 12:22 Thank you guys, take care, bye.
**Tyler Benson** 12:24 Let me know if you need, to discuss anything in more detail.
**Warre Pessers** 12:29 Yeah, sure, thank you.
**Tyler Benson** 12:32 Cheers, bye.
**Warre Pessers** 12:33 Bye-bye.
