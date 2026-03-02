SIG: Specification SIG
Date: 2025-07-22
Duration: 45 minutes
Zoom Recording URL: https://zoom.us/rec/share/94_W3ptySrbJVHOpmW_egjex5oHcaxVUiWGfPf5FaSFbterw00CuuMJxINVS-GL8.I5yQt2KbIOgQFAbs
============================================================

## Zoom Recording Transcript

**Carlos Alberto Cortez** 02:16 Hey? Hey? Let's start in 1 min, maybe 2.
In the meantime, please. Just ask your own names and any agenda item you think it's important.
Okay, let me note. And we start.
okay for the sake of money. Let's move on. Let's move fast. Sorry.
Let me share my screen. That makes sense. Yeah. The 1st item is your strask. So you want to share. I can share for you. Otherwise.
**Trask Stalnaker** 03:56 You can share
So.
**Carlos Alberto Cortez** 04:01 Tweet.
There we are!
**Trask Stalnaker** 04:10 So this came up in the Java Sig last week, and so I said I would bring it to the spec meeting. The now that we have
stabilize the trace id ratio based, algorithm hashing algorithm.
we're not sure what to do in how to handle that in Java. Because and I'm guessing other languages would have the same question.
We don't.
We're not sure it's okay. Whether it's okay to change the existing
hashing algorithm that's used in the trace id ratio based sampler in, you know, in Java.
We suspect it's not. We suspect that that would be a breaking change
and so we're imagining we would need to create a new something.
a new sampler that implements this new algorithm and would have a new configuration name
but wanted to basically ask here, what
folks thought, especially Josh Mcdonald, since you've kind of curious. If there was kind of prior discussion about how you were expecting Sigs to languages to handle this.
**jmacdonald** 05:48 Hi, so I just came back from a week away, and I haven't had a chance to read this yet, so maybe I could follow up on these issues. Otherwise I
I'm not sure I see the question yet.
**Carlos Alberto Cortez** 06:01 Basically, it's about, do you remember that we change the algorithm to use the random part of the trace? Id.
**jmacdonald** 06:09 Yep.
**Carlos Alberto Cortez** 06:10 That stuff.
**jmacdonald** 06:11 Okay? So that was, yeah.
okay, I understand. May I go to the issue itself? Is there an issue we can follow on this.
**Trask Stalnaker** 06:22 No, no, this just came up last week in the Java Sig, and so I I said I would
come to bring it up in the spec meeting.
But that's a good we can. We can give you a.
**jmacdonald** 06:34 This shouldn't be considered a breaking change, because there was never a finished specification. If you'll recall, there was a to do under trace id ratio, or since 1.0 basically saying, this is an unspecified algorithm. If you want to use it, you have to follow certain rules. And then we kind of codified those rules in the spec changes, talking about.
**Trask Stalnaker** 06:54 I agree that it's I'm not. I agree that it's not a breaking change in the spec.
But for Java users right.
it could be considered a breaking change. And so we're trying to understand, is that an okay breaking change to put on our users?
Or should we create a new, a second
sampler that implements this new algorithm.
Let let's go to some hands and we can circle back.
**Carlos Alberto Cortez** 07:28 Yeah, Robert, please. And then Daniel.
**Robert Pająk** 07:32 Yeah, I just want to call out that I think it's common for all languages. And when I just saw the differences between the specification when consuming it. It was kind of awkward that it was a stabilized part before that. Now the whole like trace id is development.
like, I think, that this. It makes things confusing for the readers, probably just the some kind of
from maybe some kind. Maybe it should be like a v 2 of this thing I'm not sure, or it should be. Maybe the part which has been changed should be in development status, but it's I think it might be even hard for the maintainers
to follow up how to basically proceed with the changes. So I think it's kind of the same which trust is right. Now, where is where is he?
That's all. From my side.
**Daniel Dyla (Dynatrace)** 08:25 Just to clarify, just to clarify the breaking change here is that now a different subset of spans will be selected. Because a new algorithm is used. So if you update part of your infrastructure, you may not have the same
you. You may not have the same selection from the same. Trace. Id. In 2 different parts of your your application is that, like the
the heart of the of the brain.
**Trask Stalnaker** 08:52 Based.
**jmacdonald** 08:56 Yeah. And so the argument has been that that great big to do in the specification from the start was saying, you can't use this reliably with, except at the root in a head-based sampling scenario, and therefore
you know the the I guess the fear is you're going to roll out your new server, and it's going to have half old versions and half new versions. And we think this is okay and not breaking, because if you only use this sampling decision at the root, then your sampling decision will be correct in both places. It will be the old one in the old place and the new one in New place, and the context will propagate, and you'll make a consistent sampling decision. You'll follow. You'll get
complete traces, which is what.
however, in some sense, you, you know it's hard to deny that we're changing the decision.
If you were breaking that to do recommendation meaning don't use this except at the root. If you were doing something that, honestly, is what we're trying to enable with these changes already, then you'd see the problem. So you were using, say, a sampler in a non head location, and that's going to break for sure.
**Trask Stalnaker** 10:00 And I don't know what I don't have a good sense of is
well, I know that we haven't communicated that. Well, via like Job to Java users specifically, if you know somebody didn't go and read the spec. So people consuming
but I don't have a sense of
if many people are doing that or not.
And so I would.
I'm I'm okay with it of with us deciding that, hey? This is, you know, we can just change it. Algorithm in the language samplers.
I just wanna make sure that that's a
community is good with that. And you know, that's the message we're putting out.
**Daniel Dyla (Dynatrace)** 10:48 Yeah, we also don't communicate this. Well in js, right now, our docs say the trace id ratio sampler may be used with the parent based sampler to respect the sample flag of an incoming trace. It doesn't say anything along the lines of like
this is the way that you should set it up, or you may have problems.
I guess that's a more of a language concern, but I suspect it's probably all language head. I doubt that very many languages. Did a great job here.
**Tyler Yahn** 11:25 I think that even if the problem is is like, even if you did document it like documentation is one thing, syntax and like semantics are another, and so like how it's used in the wilds, I think, is is important, and if you are seeing this used in a way that can be a broken change. Then I think we have a problem.
**Daniel Dyla (Dynatrace)** 11:43 Yeah, it might be.
Even if we're technically like this is not breaking, you know all of those
from a spec perspective. It may be easier
to just hand. Wave this away by renaming it to like.
I don't know. The W. 3 C. Level, 2 sampler or something along those lines.
That's probably not a good name, but you know what I mean.
**Tyler Yahn** 12:11 Sorry for.
**jmacdonald** 12:11 And then would you propose to keep that to do that language forever, saying, This is that you can do this, but you can't do it across sdks or SDK versions, I mean, like, are we gonna freeze the original implementations of those 1.0 tracer samplers forever?
**Trask Stalnaker** 12:26 We could deprecate them.
**Daniel Dyla (Dynatrace)** 12:28 Yeah, I was, gonna say, deprecate.
**jmacdonald** 12:31 Yeah.
**Daniel Dyla (Dynatrace)** 12:33 So yes.
**jmacdonald** 12:34 Yeah, I've never liked the name. Trace id ratio honestly, and we had to put special language in the spec to say, actually, it's not a trace id ratio. It's a it's a ratio computed from W. 3 C. Level, 2 trace state bits, or whatever.
So that that doesn't bother me at all. I was. I was my. This is many years of work now, but like I thought that to do in the original spec was like a nothing here works. You can't rely on anything. It's unspecified behavior. What you're doing today
do we have to call it breaking? If it's unspecified behavior.
**Daniel Dyla (Dynatrace)** 13:04 Yeah, in the spec. I agree with you.
**Trask Stalnaker** 13:07 Yeah, totally agree. Just, I think, from a practical perspective, we haven't communicated that. Well.
and so we probably have a decent number of users who are not adhering to that.
**Daniel Dyla (Dynatrace)** 13:23 Yeah, not all.
only that, but like, even if it is documented in the readme, there's a lot of people that just
you know it.
I think that if you're doing this.
**jmacdonald** 13:33 Behavior is literally not working today. So if you're using it at the head, correct, it's correct, and it works, and you can upgrade without breaking. If you're not using at the head, it's already broken.
**Tyler Yahn** 13:44 Well, I don't know.
**ap** 13:45 All the.
**Tyler Yahn** 13:45 It's it's it's making a different decision, it maybe not making the one that you think is correct. But I don't think you say it's.
**jmacdonald** 13:52 Vision, that yeah.
**Tyler Yahn** 13:53 Right. That's what I'm saying. I I don't think that's entirely fair, like, I think that you can say that it's it's working from the user's perspective, and that that behavior is what they're expecting.
And I think.
**ap** 14:04 Oh! This!
**Tyler Yahn** 14:04 Kind of brings up a good point, though, that, like the definition of the specification, if we are going to include things that are undefined behavior, or are still in development, or something like that. I think we need to do a better job like writing specification, to to communicate that, whether that's communicating it down through the implementation. Or it's in the specification saying that, like that part is literally not stable yet, and it should not be released.
**ap** 14:30 A couple of quick points.
Okay, can I?
**Trask Stalnaker** 14:33 Yeah, I have.
**ap** 14:33 Yeah, before, just in general, like, if it's literally unspecified or we are.
we are adding constraint on previously unspecified behavior that now makes specified behavior like I, we, this has come up before someone would have to check and see if we said that was breaking or not.
But this has been a topic that's been discussed. The second thing is in terms of communication. Like I,
I think that we can start to commute like.
even if we're not releasing it like tomorrow or whatever like, we can give people heads up. We can give people notice like we just need to
know when that change is going to happen, or we need to commit to whatever the change is gonna be, and then start communicating about it as soon as possible, rather than
debating. If we're going to do it forever.
It's my only role.
**Trask Stalnaker** 15:27 In this case
we have a very I. I think we have a path forward that sounds like everybody agrees on, which is just create a new name.
deprecate, eventually deprecate the old one.
right, that everybody seemed happy with that.
**Carlos Alberto Cortez** 15:44 Actually, yeah, I could only add that I think it's a requirement that we deprecate the current one because of that total node that has been there forever. So I would say, it's 1 single step deprecating that plus creating a new sampler with this new name. I think.
**Trask Stalnaker** 16:00 Well, I I wouldn't deprecate the old one until we stabilize the new one.
**Carlos Alberto Cortez** 16:04 Oh, yeah. Good. Point.
**ap** 16:06 Right like we. There is Doc. I mean, there is language for for this right now in the lifecycle docs, I believe.
like we can we? Our guidance should probably, if we're gonna make a new one, and then when the new one is stable, we deprecate the old one, then we should point people with that we should like proactively communicate. Hey.
we're gonna be doing this new thing. Here's why we're doing the new thing. If you're doing the old thing. Then here's why it's probably not doing what you think it's doing. And here is when we are going to deprecate the old thing, and then, when it is deprecated.
you will have, however, many years before it is removed.
**Robert Pająk** 16:44 We already did it for the Jaeger exporter, for instance.
**ap** 16:49 Yeah, right? Like we there, we've done this before. It's not a new muscle.
**jmacdonald** 16:53 This is great. Can we call it probability sampler? I think that would be a more natural name. Also. I I will.
I have a question
is where it works correctly. If you are using the same SDK everywhere in your system, you can do independent sampling at different children, nodes, and so on. So yes, there's something that we can break here, and you know, whatever you like we would like to do. It's fine with me.
**Trask Stalnaker** 17:17 Go ahead!
**Bogdan** 17:18 I have a question wouldn't we have the same problem if somebody is using the current trace ratio sampler and want to move to the new one?
Wouldn't they have the same exact, same problem as
we just discussed 10 min ago?
Or how how would somebody do a transition from one to another, into your fleet.
**jmacdonald** 17:43 Yeah. So this is addressed in the in the documentation that we did like, it's impossible to change trade sampling rates without breaking something. You can have 2 samplers in parallel that output half of your intended amount each that works
there are ways to do it. But every time I've looked at this like the cost of doing it correctly, as opposed to like.
There's going to be 1 min where all traces are broken. That's much much easier, much cheaper, much less cognitive load. So most of the time, that's what I seem to see people choosing to do. If you want to talk about a correct, never having a broken traces moment.
The theory is that you were already broken from that to do like you couldn't do this correctly except very carefully, before.
**Bogdan** 18:30 And
I'm I mean I'm happy but that I I cannot buy that argument with 1 min, because think about somebody with a large infrastructure would be maybe months, until everything gets upgraded.
**jmacdonald** 18:45 So, Bogdan again. This this to do that's in the spec says you can only use this sampler at the head, and if you use the sampler at the head, you will not have broken traces. That's the argument by which you can upgrade your system without breaking traces.
**Bogdan** 18:58 For it.
**jmacdonald** 18:59 However.
if you're doing some sort of fancy sampling where children are making their own rate limited decisions, maybe that you're not going to have consistent choices at that. During that transition period.
**Bogdan** 19:09 Okay.
**jmacdonald** 19:11 So again
hard to do, you cut your sampling rate in half. You have 2 sampling algorithms at once, and so on.
**Bogdan** 19:18 So would be good, Josh, since you have a lot of context, would be good to kind of write not a quick start, but best practices, or whatever not spec necessary, but some sort of best practices that you you recommend, because these are kind of things that I I would like our users to read and understand.
**jmacdonald** 19:39 Yeah.
**Trask Stalnaker** 19:39 It'd be like.
**jmacdonald** 19:40 There's a document which we should make sure it's perfect. But there is a document that addresses much, much of this, and I will go visit it after this talk. Thank you.
**Trask Stalnaker** 19:48 And then, I think, to Austin's point about communicating like having a blog post at some point. That explains it's nice. Whenever we deprecate something, I think, to have a blog post explaining why. And that could explain the transition. And maybe
even if it's complicated, we could just reference the existing Doc, that you have Josh on the upgrade.
**jmacdonald** 20:13 Yeah, I really wanna make sure south coast.
It's hard to make a post when nothing's done yet, though. So I think we need to make some progress.
**Carlos Alberto Cortez** 20:20 Yep.
**Bogdan** 20:22 Yeah, my, my vote would be the same as the others to to go with a different name, since it simplifies a bit all the the language, and makes people more aware about this change.
**Carlos Alberto Cortez** 20:35 Okay, that seems like a plan. So yes, translation. We, I think we have a path forward
who will be? I mean, either trust or Jim Mcd or myself. We can create the Pr and issue and all that.
But yeah, otherwise, it's clear we have a initial path forward.
**Trask Stalnaker** 20:50 Josh, is this something that the sampling Sig can drive.
**jmacdonald** 20:55 Yeah, definitely. So I I will take away from this conversation an action item.
**Trask Stalnaker** 21:03 You all can pick. You all can pick whatever name you like.
**jmacdonald** 21:07 Okay. Thank you.
**Carlos Alberto Cortez** 21:09 Perfect. Thank you so much for that. Yeah. Okay, let's move on. We don't have many items, but still, let's try to
to move on. Make progress. Robert. Yeah.
**Robert Pająk** 21:20 So because you already like 20 min already passed. So I just proposed to not even open this Prs just to mention to to to review it. If someone is interested, they mostly have a lot of reviews, and they are not critical like they're all mostly clarifications backfixes in the specification. This one was discussed last week, and it already got approved by Jack.
So I think it's good to merge
the second one is regarding the configuration SDK, and it has been already approved by 2 maintainers of the configuration stick and one approver.
So also just a kind of
almost nitpicking just the names were make were misleading.
and the 3rd one is also from some user reported that the protocol, the Otlp protocol default, is kind of not consistently defined in different places of documentation which was misleading.
So it's just about kind of copy pasting the same defaults in in the other place.
Yeah. And that's all for these 3 prs.
and.
**Carlos Alberto Cortez** 22:45 Yeah, you want to say something.
**Robert Pająk** 22:47 I think we can go go further
to the next topic, which is more complex. And I added few 10 min. So basically last time last week the auto of extending attributes has been merged, but I wanted to start making some baby steps because it's a it will be a very
it will be very impactful. And the 1st Pr is basically like a preparatory prep
preparation for the changes.
So the because right now the restrictions on the attributes were only the specification
I propose in this Pr to also add this kind of restrictions to the proto definitions. Right now it was only in one place in the trace attributes, and it was only referencing.
referencing, like the specification which can change.
So instead of this, I try to explicitly add this kind of type restrictions
on the attribute types in the, in the proto, in the proto definitions, thanks to it in future, when we will be adding new attribute types to all signals. We'll be able to communicate it via change, log and change of the comments, etc. I think it will be a better users. It will be better for the people who care about the protocol definitions which which basically trade the change log for the for the
like endpoint implementations so they can read and follow and adjust as needed.
You can show the file changes and just give one example, and maybe just scroll. And here's an example.
So I use this should not. I'm just explicitly trying. Try to call out all the types that were not supposed
to be handled according to the data model of different signals I put should not, because
it's nothing that 1st of all, it's nothing that we kind of are able to people's, they can still do it. We just do not recommend doing it also. Some people are already handling it, and even the collector
is still even passing this forward. So even kind of the collector, if someone sends an empty value, it will be already. It will already go for the collector. So you just wanted to, basically. But I feel that having this language here is basically our current status and our current basically art, how how we see the attributes
and then moving forward. We can just kind of
change each kind of type, one by one, for instance, and go forward with this.
Does anyone have any questions? Because I think I'm have spoken a lot already.
**Carlos Alberto Cortez** 25:42 Is it the same comment? Exactly.
**Robert Pająk** 25:43 Yes.
**Carlos Alberto Cortez** 25:44 With them.
**Robert Pająk** 25:44 Exactly the same column, just in different places where attributes are present
because it's not there in the attributes of a log record, when everything is possible, even according to the data model.
**Carlos Alberto Cortez** 26:08 No comments. I think.
**Robert Pająk** 26:10 Okay, so we can go to the other one.
**Carlos Alberto Cortez** 26:14 And of course, consider reviewing that, please.
**Robert Pająk** 26:16 Yeah, especially, it's a proto change.
**Carlos Alberto Cortez** 26:20 Right.
**Robert Pająk** 26:20 So so if you maybe just
so this is this, Pr is basically adding the 1st type to the standard attributes, which is the empty value.
and we find it especially important.
because if someone would like to reuse the standard attributes for the lock signal for the logs, Api.
without having the empty value.
It's impossible to implement the body which by default is empty.
Basically.
So if someone wants to use the attribute value types in the logs. Api.
it's impossible even to right now. Implement in a, it's impossible to implement.
someone will just need to create different types. And I even put, I checked how other implementations which are stable logs. Api, how have done done it? So basically, Java has it packed up as a string.
and the value type of the attribute does not allow setting empty. So the Ph, if you scroll down, I think I listed it the I think it was Php basically accepts anything.
So basically, it's like a kind of any object can be passed which kind of is not also perfectly specification compliant. And it.net. It was kind of the same. You can pass any object if I no, it was a string. The body was also only a string.
so regarding the changes. If you open file change, I only propose to add
this new new attribute type, which is an empty value with a development status.
So that's the only basically change. And also I removed some places
from the specification which disallowed using an empty attribute value.
**Liudmila Molkova** 28:22 So we had a discussion on this Robert and I
the thing I'm trying to solve. For example, python folks are considering just going
onto the complex attributes now, but not we. It's not what we wrote in the autop, right?
We want people to not stabilize it until 6 months from the last week.
and I feel we need some language in the spec that would explain maintainers that they are.
even though they can implement it. They cannot stabilize it. Yet.
**Robert Pająk** 29:00 And if we just doesn't, doesn't specifying it as a development status, Paul calls it already.
**Liudmila Molkova** 29:07 No, no, the empty value is fine, but removing the restriction on the
extended attributes, I feel we need to replace it with some warning, saying that they will be allowed in the future, but not yet, so don't
go and enable them.
**Robert Pająk** 29:29 I see. So this part of the specification which was telling that it may might not happen. You want to additionally make some notice before the specification
right.
**Liudmila Molkova** 29:41 Yeah, I'm struggling to find the good words. Maybe I can spend more time thinking about it, or we can talk about it in the logs.
**Robert Pająk** 29:50 Yes, I think it can be good to have it separated. Then I can remove the changes from this fragment, which says that they cannot be changed and leave is that it is. And we can create 1st a Pr which will just say
that these are allowed and make a separate change log. Notice that this can happen in future, that it is not longer seen as a breaking change, or things like that. It makes sense. It may, it will make the communication better.
**Liudmila Molkova** 30:18 Yeah, thank, you.
**Robert Pająk** 30:20 Any other comments.
Okay, then I think we can go with the next topic. Thank you.
**Carlos Alberto Cortez** 30:33 Tweet Lydmila you want to share, or I share of them.
**Liudmila Molkova** 30:38 Yeah, actually, I want to share. If you don't mind.
**Carlos Alberto Cortez** 30:41 Perfect.
**Liudmila Molkova** 30:43 Yes. So we are starting to social socialize. The otap. About exceptions and logs are.
I'm here today to kind of collect some high level feedback. It's in there. Let's say it's in early stages. There are 264 comments on this setup already, but we extracted parts of it into the span event. Deprecation.
and I feel most comments were about spend event deprecation. So now this tab is the next step we are trying to tackle in the log space.
Okay, so let me guide you through a few things. I think there are 2 important parts here.
First, st we used to have record exception on spans.
Without span events we would still like to have a way to record exceptions. Slash errors
now on logs, right? Because we believe that if you record just the exception.
there's maybe some context, it probably belongs on logs. You may be able to record it as span attributes. But that's a separate story. So one, if you want to record them on logs.
the setup suggests some guidance.
And 1st thing it suggests is, okay, let's have a set exception method on the log record, or some means to provide the the whole exception. Object to the log record
from now on. This allows us to do all kinds of cool things. We can decide if and how we record stack, trace.
right? We can customize it. We can drop it. We can.
I mean, we we, I think essential part is is we can customize it. It's the logic of the SDK that can be driven by user configuration.
The second part is that, okay?
When we recorded exceptions on span events, we didn't have a concept of severity.
And now we do. We have severity on logs.
and the presence of exception does not indicate an error. Necessarily.
Sometimes you get an exception absolutely about absolutely benign things. You just robe, for example, that you are on the right version of Java and turns out you're on Java 8, and you don't have some runtime some Api and Runtime
or you. You're just checking things. And
because war world isn't perfect, things are exceptions. And they.
They are not indicative of any problem. Maybe you should set severity debug on on certain exceptions, you might still want to record them.
And some exceptions are severe.
And this attempt suggests some framework on how you set severity based on the
based on severity of this error.
I would expect it would be somewhat controversial, and we would need to bake. Shed a little bit on this one. Let's see. But I would I would be interested in gauging your feedback on a
section that goes through different
ideas for collecting, for setting severity.
Let's get to it.
But let's assume we set it somehow.
And then the problem that happens today
is that 1st people tend to record exceptions. Anytime they
handle them or they write some code, they add a catch block. And the code above this code will also have a catch block, and every time they let's say.
see any exception, they would record a log about it.
This Tab proposes that, at least in the
good behaving compliant with open telemetry world. You probably don't want to do this. You're recorded when it happens.
and then, if you are re throwing it as is, you don't record it anymore. You hope that somebody below you recorded, and then, if you know they they're not.
you'll probably want to record it as well. But just once.
The second part is the exception. Stack traces are huge.
and you really don't want to record them all the time.
And like, I can speak about azure monitor that we in azure monitor, we try to record them when exception remains unhandled.
So let's say, in my client library.
I'm going to throw some error here.
But user code above it is likely to handle it.
Maybe retry, maybe ignore.
Maybe it made some reasonable. I don't know. 5 0 3 for a 29 status that they've they've handled it.
And only if it remains unhandled all the way to let's say the Controller level and it escapes user code. Then
we would actually want to record stack traces we can make this configurable in this way.
So let's say, the severity is in full.
We might not need stack, trace
or if it's error, we probably do need it, it becomes more important to record it.
So this setup suggests to introduce a threshold, a configuration parameter controlling at which level stack traces are recorded.
And it suggests to have an error as the level where they are.
Of course it's customizable. Somebody can write the the thing that reduces stack, trace and makes it
smaller and more usable.
But this is the 1st step we'd like to introduce here.
So I think I gave a high level overview of what we're going to do here.
Yeah, Josh, go ahead.
**Josh Suereth** 37:49 So the I I like. I like the features that you have in this. The filtering of error. Is that
Is this going to be like a log processor that would be like configured by default in the SDK kind of a thing? Or is this like an SDK thing that would happen before or after log processors, of how you do stack, trace
like, what? How?
How do we plan to engage with that in in the in the config? And is there a way we can make it like
flexible, like a log processor? And is is that worthwhile, or am I over complicating it?
**Liudmila Molkova** 38:24 I think we, we can approach it in 2 ways. My thoughts were that the SDK would implement set exception
alright, and it would interact with configuration.
We could have a thing called, I think there is some proposal
from some Java person about having a customizer to record stack traces.
It could be part of SDK configuration. For this method the other approach would be to actually pause the whole exception through the processing pipeline and then have a processor. I don't have an answer yet, but that's a good feedback. We should figure it out and document it.
Okay. Any other questions or thoughts.
Okay, it seems there aren't. I would add one more thing. We are.
still figuring out what it would mean, for, except for languages that don't have an a concept of exception.
Some parts of it would apply, some others wouldn't.
And if you work on this language.
please send your feedback. One would be super happy to consider it, and definitely having a prototype in one of these languages would be a requirement to moving forward with this setup.
Okay.
**Trask Stalnaker** 40:09 Kind of broad
comment for of for languages. One of the goals here is to currently how, where, and how we record exceptions. Varies a lot across languages and across instrumentations in open telemetry.
And so part of the goal of this Otep is to
have an opinionated way that is recommended.
And so at some point.
we'll need to engage with what that means for existing instrumentations. You know how they would migrate to this new guidance.
Probably it would be something kind of similar to you know. We we won't introduce any breaking changes on the SDK side, but for instrumentations to go from where they are today. To following this guidance would be breaking to their users. And so it's probably something similar to like
when we updated broke Http semantic conventions right? Like that, instrumentations needed to do some kind of graceful ish
transition.
**Liudmila Molkova** 41:40 And they have some of it documented in the Span event. Api deprecation plan.
Okay. So if there is.
**Trask Stalnaker** 42:00 Kind of to
just for people. When you're reading this, there's kind of 2 different questions there. One is, what's the ideal like? There's the ideal end, state the opinionated defaults and configurability. And then there's the yeah. The transition plan.
**Liudmila Molkova** 42:39 Okay. Any last minutes concerns questions.
**Carlos Alberto Cortez** 42:46 Probably should it should be on draft. We already discussed that in the past, and probably people are waiting that this becomes, like, you know, stable Pr, to review that. So for your consideration.
**Liudmila Molkova** 43:00 Sounds. Good. Yeah. Thanks.
**Carlos Alberto Cortez** 43:06 Okay, I hear no comments. So I guess this is it.
So going once, going twice.
Okay. In that case, that's all for today. And consider reading some of the Robert W. Miller's, Pr. So thank you so much, and stay safe. Ciao.
**Trask Stalnaker** 43:25 I.
**Reiley Yang** 43:27 Thank you. Bye.
**Liudmila Molkova** 43:27 Bye.
