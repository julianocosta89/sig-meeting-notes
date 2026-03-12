SIG: Specification SIG
Date: 2025-06-17
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/bEe2IrLlGEk-DYb9Y_0H9ddoyTZLpYlW7H6zYiIgFRzredEz4IwMlakwzfcqfG_u.GtO8OpAG29yEW5ry
============================================================

## Zoom Recording Transcript

Tigran Najaryan 00:01:33 Hey, guys.
Ted Young 00:01:38 Yo yo.
Trask Stalnaker 00:01:45 Hey?
I'll take care of our note taker, friend.
Tigran Najaryan 00:01:56 How do you take care of it? You know. What do you do?
Trask Stalnaker 00:02:01 There's a in the community repo. There's a a section on zoom bombing prevention.
That will always have to go to, and it links to a document that has the host keys and then I click on the little green shield in the meeting to see which host. This is.
and this doesn't have, an it's doesn't have a number on it. So that means it's this number 0, and then go to the participants list, and you can claim host with that number.
Tigran Najaryan 00:02:43 Okay.
Thanks. Trosk.
Trask Stalnaker 00:02:46 Yeah.
And then you can remove them and optionally report to Zoom, which I have. I always I I do, but they always tell me that this is not a violation of anything.
Daniel Dyla (Dynatrace) 00:03:02 What are the chances that it's just like a community member adding their note taker thing.
Trask Stalnaker 00:03:13 Probably.
Daniel Dyla (Dynatrace) 00:03:15 Is that not allowed? Is, are there specific rules against that.
Trask Stalnaker 00:03:26 Specific open telemetry or zoom.
Daniel Dyla (Dynatrace) 00:03:29 Yes, open telemetry, I assume Zoom doesn't have any such rule, but our does open telemetry as an.
Carlos Alberto Cortez 00:03:34 Or hey? Sorry for being late.
Daniel Dyla (Dynatrace) 00:03:36 The rules against that.
Carlos Alberto Cortez 00:03:37 Use that.
Oh, sorry! Were you saying something sorry for interrupting.
Daniel Dyla (Dynatrace) 00:03:41 No, you're okay.
Trask Stalnaker 00:03:44 I think. It kind of falls under the the reason why people didn't want these recordings posted on Youtube.
And so we started because they didn't want people scraping them.
So I mean we don't. If we knew that it was a particular member, and they said it was what they were doing.
I think that would be okay.
Daniel Dyla (Dynatrace) 00:04:12 Yeah, I mean, I don't disagree with the with the action of of you know kicking them out, or whatever I just maybe that should be documented as a policy somewhere, because it's it's entirely possible that it's just somebody that you know works at some company that uses open telemetry that wants to follow and not spend the time to join the meeting, or something like that. Who knows?
And they may not know that there's a policy about it.
Ted Young 00:04:43 I think we.
Trask Stalnaker 00:04:44 And that we record them already.
Ted Young 00:04:47 Yeah, I mean, I can see the that there's like a subset of use cases where it's like useful to somebody. But because, you know people within our community have some concerns about like how the recordings get handled.
We'd like to stick to a policy of like we provide a way to review the meetings if you're interested in doing that, and thus there's no need to.
Daniel Dyla (Dynatrace) 00:05:14 To be clear. I don't disagree with that policy at all. I just think it should be a documented policy like something that says we don't, you know. Please don't use 3rd party recording tools of any kind, including AI note taking tools and that way. For one thing, I I don't think people.
if it is just a community member, we're way off topic for this meeting now. But if if it is just a community member, they probably wouldn't have read that rule to begin with, but if they notice their bot being kicked out of stuff consistently, they may get irritated and complain, and then we can point to a rule and say, Hey, look! We have this. No, no takers rule.
Ted Young 00:05:57 Yeah, that's reasonable.
Carlos Alberto Cortez 00:06:04 It sounds like. Probably somebody should follow up on this. I don't think Dan is the correct person, but if it's like, since you're interested in this product worth following up up to you. Of course.
Daniel Dyla (Dynatrace) 00:06:19 Yeah, I can. I can open a community issue or something at the I guess the only concern that I have is that we shouldn't have undocumented policies. I don't particularly have a strong opinion about this particular policy.
Carlos Alberto Cortez 00:06:37 Yep.
that makes sense. Okay. Let's start. Then the meeting. Sorry for being late. Sorry for interrupting to, you know, like my Wi-fi was doing weird things right before the meeting. Okay, so the 1st item is mine. It's just, you know.
just for you to know that a pair of items in the logging area were were merged.
Both of them are important because they are, you know, stabilization of a lot of items.
So want people to be aware of that, you know, especially maintainers. Of course.
the 1st one is event, name.
the second one is the SDK portion of this one. That Bob, Robert, did you know? So for your information, I think it's important for Maintainers to know, as I mentioned before.
one small question that I have about this is Robert here. By the way.
Robert Pająk 00:07:28 Yes, I am. Hello.
Carlos Alberto Cortez 00:07:29 Hello, thank you so much. Yeah. I was mentioning the docs that it's funny, because we don't like this is the of course, SDK. Portion of the enabled operation, and we are not mentioning the parameters.
and these enable most return false, otherwise it should return through, doesn't take into account. The parameters like severity or events, name. I don't know whether it's worth verifying that parents.
because these sections looks like no parameters, were provided, you know. And it's always probably, for people who have been involved in the project. Well, for a person coming and the friend of the men this is like, Hey, wait, you know. There are parameters mentioned in the Api section, and then the SDK doesn't mention them.
So yeah, probably we can disclose out of line. If people think.
Robert Pająk 00:08:19 Simple.
Maybe we have. We could just link at that statement that this is implementing the Api interface and going back to the Api some reference.
so that we don't copy paste, but.
Carlos Alberto Cortez 00:08:34 Yeah, I think, yeah, that would be good, in my opinion.
Robert Pająk 00:08:37 Okay, we can take it offline. I will try to submit a Pr. If I do not forget.
No worries. I can do that even forget. So don't worry. So that. But yeah, I think it's pretty clear.
Thank you.
Carlos Alberto Cortez 00:08:49 Perfect next one, Ted, you want to share your screen. I can do that, and it's 1 min. So probably it's short.
Ted Young 00:08:54 Oh, yeah, no need to share the screen. Just Just an fyi, the browser Sig phase one has been approved as a project. So we'll be having our 1st meeting. This Thursday meetings will be Thursdays, 8 30 Am. Pacific.
We're trying to have a 30 min meeting. We'll see how that goes. Maybe that's a practice we can extend to other sigs.
So if you're interested, please join.
that's all I got.
Carlos Alberto Cortez 00:09:33 Perfect. Thank you. So see, you see you there.
Okay, the next one is mine. Probably we can use 5 min for that this is filled by urassi. So pr you may not remember. But there was an auto 2, 3, 2, which updated the lifecycle faces to make things more uniform.
And basically that this change is bringing that part from Delta into the actual spec.
The only question remaining, and is so, Josh.
The call is whether feature. Freeze where it's out whether the feature freeze will could be a separate.
a descriptor, let's say, independent of the actual live face or whether this should be part like we should, we should disappear and become part of I don't know. For example, release candidates.
and the current approach is that feature freeze is a separate descriptor, you know.
Like you can see this one description by degree. Grant the feature, please, is not a maturity level.
It just would mean that we are not accepting new changes.
Josh, you want to say something about this.
Any comment, or you're fine with this. Oh, yes.
Josh Suereth 00:10:58 So was that was that me, Josh or the other Josh.
Carlos Alberto Cortez 00:11:01 Yeah, some of you. Yeah, yeah, correct. Yeah.
Josh Suereth 00:11:02 Yeah, I I yeah, I guess the the question I have is, is, that's how we were using feature freeze. Do we still want it. For that same reason, I'm trying to think like the 2 areas of the spec that I expect to change mo like re like now given sigs that are active.
In areas that could use feature freeze is profiling and entities right where we have a section of the spec where we can actually move it into experimental and then feature, freeze. But honestly, to me, feature freeze would be release candidate like as an entities. Sig. Author. If we take the entities thing, and we get to the point where we say, Okay, this is feature complete.
That's almost like saying, we think this is release candidate right?
So from my standpoint, I actually don't know if I would use feature freeze going forward.
For this If we wanted to assign feature, freeze to existing parts of the spec. That's another question of like, okay, we have a stable part of the spec, and we actually don't want this piece of the spec to ever change.
Is that any different than deprecating that piece of the spec at that point? Or is it like we're just giving a signal to people. We don't want them to make changes.
you know.
So that's kind of how I'm thinking about this of like, yes, feature freeze means something different today. But in the future, how will we use it? And will we use it in a way that means something different going forward like, do we still need that I I could go either way here. It doesn't. It doesn't bother me to keep it. It doesn't bother me to get rid of it. I think that from the standpoint of like the work that I know going on the spec, I think we can use release candidate just fine.
Trask Stalnaker 00:12:54 I think feature freeze has been a source of confusion a number of times in the past, and so, if we think so, if we don't need it, I would vote for removing it.
Ted Young 00:13:16 Yeah, yeah, the traditional use of feature freeze was to focus the community right? Like, it was a focusing tool.
Where we wanted to assign feature, freeze to parts of the spec, just to indicate that we were no longer. We were not currently accepting changes to that part in order to get the community to focus on a different part.
feels like we've kind of moved beyond that phase of open telemetry where that's a useful way of performing that particular task.
so I would be fine with retiring. It.
Carlos Alberto Cortez 00:13:57 Yeah, there, there's an option about bringing it back later on, if needed, and remove it for now. That's also an option, of course.
Tigra, do you have an opinion about removing feature? Freeze.
Tigran Najaryan 00:14:09 I mean, I I don't mind if we want to remove that. I think that's an orthogonal decision. This is about stability levels. And I don't see feature freeze as a stability level.
We can make that decision independently from rolling out this sort of.
Carlos Alberto Cortez 00:14:26 Yeah.
okay, so okay, I think you're actually not in the call. Well, let's, I will leave a comment on that one that Pr can just not touch feature, freeze, and in a separate Pr just will remove that.
Okay, perfect.
Thank you so much for that. Next one. Robert, you want to share, I can share for you, otherwise.
Robert Pająk 00:14:50 You can share. I do not want to spend a lot of time given just like discuss like so like during the last 3 meetings. I think so. It's more just here. We have most approvals. I just want to ask many the original logistic approvals to take a last look before merging it especially, I think, Tigran and Jack to double check this one. Maybe there are also others, maybe Rayleigh, for instance.
It's not a big change I try to put. So the changes are not big. I try to put a lot of in the description in the peer description. The reasons.
and I think we can go to the next one unless nobody has. If, unless there are questions.
okay, let's follow up. Then. Yeah.
Carlos Alberto Cortez 00:15:47 Tigeran is in the call, but it's up to Gigan. If you want to comment, offline, or.
Tigran Najaryan 00:15:51 I'll take a look. I'll take a look offline. I haven't had a chance to read this. I will do.
Carlos Alberto Cortez 00:15:57 Perfect. Thank you.
Robert Pająk 00:15:59 And the next one is kind of related to clarify the lock record severity comparisons. So just a recap from the last spec meeting where I think T. Grand was offline. So remember, tech run you originally wanted just to allow the values for severity from one to 24, or maybe maybe also 0 as optional.
But basically, during the last seek meeting, maybe even previous one as well. There was a more preference to just say that all basically numbers, because in most languages the severity is basically represented as a, and then which is back up by the integer apart from Java and Rust, but still, when it is converted to Otlp, it's still a number. So the preference is just to basically say that, like, simplify and clarify, clarify the local record severity comparison.
So I tried to put some comments here that we were being discussed, also offline and some reasonings. And and also I think it's better to just take a look and review it. Offline.
In my opinion it's just good to have some decision, whatever it will be.
because right now it's kind of not clear how a severity outside 1, 24 range should be compared, and even the 1 24 range is also not well described right now. It's kind of hard to guess what the authors had in mind, or what is maybe even what what is the what, what, the how, the maintainers. How should implement it? And yeah, that's all from my side.
Tigran Najaryan 00:17:49 You're suggesting that we allow values outside that range or something else.
Robert Pająk 00:17:54 Yes.
Tigran Najaryan 00:17:54 Yes, this.
Robert Pająk 00:17:55 Yes, this was the. This was the summer of discussion that basically these, the values between way one and 24 have basically semantic naming rather the values outside can be also used, but they just do not have semantic meaning from the open telemetry standpoint. I think that was the conclusion.
Tigran Najaryan 00:18:19 I mean, when we talk about the values outside the the I guess below, I guess we're not talking about negative values. I'm I'm guessing right? It's probably not not a great way to express severity. So that would be 0 and values above 24 is what you're suggesting, we allow.
Is that correct?
Robert Pająk 00:18:41 The suggestion was also to handle the negatives for me. I have okay.
I think that. Or are you doing someone.
Ted Young 00:18:51 Sorry you can finish.
Robert Pająk 00:18:53 No. So I just want to say that for me like, the reason was simplicity. And just to have a standardized in digital ordering, because it will be simpler, for you know, just SQL and stuff like that, and just allowing 0 to be handled differently. Optionally, if someone wants but just to have a simple mechanism for comparing as possible. That was the reason, and just not to make it harder than necessary.
Ted Young 00:19:23 Yeah. And I was just gonna chime in the the reason why we have to do it is because in the data model it's represented as an integer right like back ends.
are forced to deal with the possibility of getting a negative number. So we it would be better to define what to do than leave it undefined. And the simplest thing to define is to say, you do. You know a numeric comparison with 0 being the only exception. Right? So that's it's not that we're suggesting. People use negative numbers. It's just we don't want to leave undefined behavior in the spec, for backends to deal with.
Tigran Najaryan 00:20:02 So in the, in the product, in Otlp it's not an integer, it's an enumeration.
It's defined as an enumeration. So any?
Yes, proto. Obviously, there's no way to enforce values being outside that range. But that applies to any enumeration in the proto.
Then by that argument you can say that you have to be prepared that any other enumeration in proto can contain a value that is not defined in the portal itself.
which would be essentially the typical way to react to that is to say, that's an invalid payload, and you treat it as invalid data.
I don't know why this needs to be different from that perspective.
Ted Young 00:20:46 Because with most enumerations, you're not performing a less than or greater than comparison is like the primary thing you're doing with the enumeration value. I would say like, that's the difference here.
It's because that's how it's it's kind of intended to be used as a severity level.
Tigran Najaryan 00:21:07 Okay, fair. But okay, let okay. Let me. I guess I think I'll take a look offline as well. I'll comment on it.
Trask Stalnaker 00:21:17 What does the proto buff when it deserializes the payload? I guess.
What is the Grpc standard deserialization do for out of bound numbers? Does it push those into 0.
Robert Pająk 00:21:36 It depends on the language, it depends on the.
Tigran Najaryan 00:21:38 I think the implementations don't care the ones that I saw. They don't care mostly.
Well, May, maybe you saw implementations, Robert, in some languages where there is any sort of enforcement during this realization.
When you say it depends, what what do you mean by that? Have you seen any implementations do anything about invalid values.
Trask Stalnaker 00:22:04 I think in Java they're modeled as actual enums, and so it would have to do something. It can't store the invalid values.
Jack Berg 00:22:16 I'm looking at the Java implementation right now, and if the number isn't in the range of the known enum values, it returns null , which will ultimately throw like a null pointer. Exception when you try to.
you know, interpreted as an actual unknown instance.
Ted Young 00:22:33 Robert. Maybe the middle ground here is just to to like, clarify in the spec. You should stick to this enum range like that's the intended behavior, but, like like like, add this as a clarification in the spec, but add it, you know, clarify that you should stick to this range.
but if you encounter a value outside of this range like this is the comparison operation you should use.
Robert Pająk 00:22:57 I think there's already. There's already a nice section which says that open telemetry defines kind of this one to 24 range, and this is the place where open to get semantic meaning. I would rather do it in a separate Pr. If it's not clear enough, or maybe I will accept suggestions.
But I try to. Yeah, make it more more clear and also shuffle a little bit the the if you show the changes, maybe. Carlos.
I also try to move a little bit some sections to make it more logical.
Carlos Alberto Cortez 00:23:29 Sorry, up or down. What do you say?
Robert Pająk 00:23:32 Changes the commit like the Pr change.
So I basically even right now in this, Pr try to shuffle a little bit yeah.
defines. So the following table defines the meaning.
maybe open telemetry, meaning or semantic meaning not sure. Maybe we can improve this line 294.
So I was already shuffled all these little bit the description to make it more logical.
Tigran Najaryan 00:24:05 I mean, if if, Jack, if what what you said means that? Well, essentially, it means we, we can't encourage using any other values at all right, because it's it's gonna result in problems when deserializing in Java. At least, that's what you said. Right.
Jack Berg 00:24:22 Yeah, and the you know the default implementation of you know the protobuf bindings. It would. You know you could come up with your own implementation that parses it manually and have different behavior. But the default is gonna yeah, they probably diplomatic.
Tigran Najaryan 00:24:38 I think that's a that's a strong reason to me not to allow this not to encourage this at all. Right.
keep it tight with the just, the values that are in enumeration, and and so.
Ted Young 00:24:53 Me.
Yeah, I mean, I think there's just like an easy middle ground here. I mean, it's like a tiny Pr, but Robert, like clarifying like you're doing a numerical comparison. 0 is special. And then saying, like, you should stick to this defined enumeration range.
you know, like just you're removing that line entirely, and I'm just suggesting, like, bring that back in to to make it clear, the intention is to only be comparing one to 24.
Yordis Prieto 00:25:27 Yeah. By the way, in product buffer, most of the time you specify the 1st value as underscore gonna specify for this reason.
So it's like a safe fallback value that people should respect.
And that's that's what we have here in the proto as well. What you're describing is exactly what we have in the product.
That's normally what most people are accustomed to in my experience.
Josh Suereth 00:25:56 Yeah, I was. I was, gonna say, the Java behavior. Are we accidentally compiling Java with proto? 2. Because protos like enum should be open in proto 3.
Daniel Dyla (Dynatrace) 00:26:06 Yeah, so I.
Josh Suereth 00:26:07 Everyone is consistently using proto 3. It should.
This shouldn't be an issue.
Daniel Dyla (Dynatrace) 00:26:13 No.
actually that that. So I linked a documentation page from protobuf dot dev in the in the meeting chat here.
Which explains some of this. There's a line in there that says all known Java releases are out of conformance, it says, or like right in the documentation here.
I think there, there's a big gap between things should be, and what things are, and what things are specified to be.
And I think because of that gap.
the safest thing to do is for us to treat all enums as closed, whether it's possible for them to be open or not.
Trask Stalnaker 00:26:51 Just to clarify Josh. This doesn't affect open telemetry, Java, for 2 reasons. One, we write our own bindings and 2. This is the deserialization piece, which is only server side.
Josh Suereth 00:27:04 Right? Right? Yeah, agreed agreed. But it still affects any Java user of Otlp, which is.
Daniel Dyla (Dynatrace) 00:27:12 Lot.
Josh Suereth 00:27:15 Yeah, okay, I don't.
This is so.
Tigran Najaryan 00:27:19 And and for that reason, George, I think we shouldn't allow that precisely.
Daniel Dyla (Dynatrace) 00:27:24 Known issues. Section of this page is crazy.
Josh Suereth 00:27:28 Yeah.
This. This seems like we need to restrict otlp rules now around inoms, and we should probably I mean, I hate to say this? Do we have to fake a nooms and proto going forward be for this reason.
Daniel Dyla (Dynatrace) 00:27:44 Take in what way?
Josh Suereth 00:27:47 So so the way you know, a proto is the way an enum is on on in the wire is it's just an integer right effectively or a variant.
So should we just have variance with known integer values in proto from now on. So we can have open enums. Anyway, that's a different discussion. We can take that offline.
Carlos Alberto Cortez 00:28:07 Let me know!
Liudmila Molkova 00:28:10 Yeah. So from consumer side, you know, should always be open. It doesn't matter whether we keep them closed or open. It doesn't matter. All consumers should think are open, because this gives us the way to extend them, maybe 10 years from now, but otherwise it will be a huge pain.
Robert Pająk 00:28:30 But this. But yeah, but the the receivers can be Java implementations.
So I kind of understand the concerns that because of the way how it is implemented, like from technical pers reasons. I understand why people want to have it closed because it may not be. People may not be able right now to kind of make a spec compliant implementation in Java. Right vendors am I saying correctly, trust Jack.
Jack Berg 00:29:02 Spec compliant, in which way, like what.
Robert Pająk 00:29:05 Meaning either. Maybe right now in Java, like, if the server will be in Java, the Otlp, the Otlp endpoint will not be able to basically parse, which will be minus 5, 27, because they will just back up to null right.
Jack Berg 00:29:25 Yeah, So I think if so, you can. You can represent this in a number of different ways, right? So like, you're parsing an Otlp payload, and it's got a log record. It's got this severity number in there, and you know you don't recognize the enum value that it is. It's negative 5, and that's not in the set of enums you recognize you have a couple of decisions. You can say, like, Hey, I want to represent severity as an integer when I store it on disk somewhere, or you could say I want to represent it as an enumeration or a string, or something like that, like the string equivalent of that integer when I store it on disk somewhere. If it's the integer route, then you could say like, Hey, I don't recognize negative 5. But I'm still going to store negative 5, or you could say, I don't recognize negative 5. So I'm just going to assume that it was unset, like, yeah, like, it's equivalent to not having any value at all to it being 0. Or I'm trying to think if there's an alternative to that, or if those are the 2 possible things like, and I don't. I don't think it's clear what the spec says you should do here.
Yeah, I think you're free to represent it. However, you want whether in your back end.
Daniel Dyla (Dynatrace) 00:30:46 So Josh asked if it can be an error if you're deserializing, I mean, I I don't think anybody would want to drop the payload, so they're treating it as the same as undefined, or whatever would be. I think I that would be essentially treating it as an error. I I think if we define any sort of behavior for it, like if we say out of bounds, values are numerically compared. We're just encouraging people to do that, even if we say Please don't.
people will be like Oh, well, I need something less than one, so I'll go with negative one, even though the spec says not to it also says they should be numerically compared. I think we're just encouraging people to do things we don't want them to do I would be in favor of just saying anything out of what's defined here is treated as 0 and and move on.
Robert Pająk 00:31:45 I will. I will do my homework later, unless someone objects.
Ted Young 00:31:53 I'm I'm in favor of that. I think the new information for me here was like.
Robert Pająk 00:31:58 Java.
Ted Young 00:31:59 That that proto buff implementations themselves do different things in response to out of bounds enum. So like, we're not doing anyone a favor.
Robert Pająk 00:32:10 You buy it, I agree.
Okay, thank you. Let's go further.
Thanks for feedback. Everyone.
Carlos Alberto Cortez 00:32:23 Yeah, thank you so much for the patience. By the way, it has been taking some time. But yeah, let's see how that goes.
Okay, the next item I guess the Miller transport is one here. You want to share.
Trask Stalnaker 00:32:36 I think. Actually, Robert added it, but I couldn't drive any of us can so yes, I think Robert is Antsy to get this merged because the go folks this is blocking their log work. So yeah, we've been struggling to get more approvals on it. I would really prefer to have more approvals on something this big. But it doesn't necessarily require more. It's So anyway, it's basically a open question to folks here.
Should we go ahead and merge it as is is there any chance of getting additional folks to review it? And or my worry, of course, is, does lack of engagement on it mean that people are.
you know, basically like lukewarm, like not really in favor of it. Getting merged.
Ted Young 00:34:02 I think it's a hard thing that has no good answer right?
But we decided that having a uniform model was like the lesser of 2 evils here, and it was worthwhile to to have this potentially breaking change in order to do it.
So we're gonna do it but it's not for an issue like that. I don't think it's possible to come to like glowing endorsement from everyone just due to its nature.
Trask Stalnaker 00:34:37 No, but we can. People can say, Yes, I I agree that this is.
you know, the way we're gonna go forward.
Tigran Najaryan 00:34:51 I think I personally support.
I'm reviewing it right now. We'll comment on it. I support the idea.
but I may have some comments there about the actual implementation, I think, for something like this, we should look at well, not necessarily consensus, but significantly larger number of approvals on an issue like this.
since it has a like a significant past history of wanting. Not wanting to do this. Again like I said, I personally support. I'd like to see more more approvals there, more green check marks.
Carlos Alberto Cortez 00:35:30 Yeah, I would even say that I would love to see approvals, or at least reviews, even if you don't feel comfortable with from maintainers, you know.
at least to know that they are not totally opposed. You know.
Ted Young 00:35:50 How do we go about getting that.
Trask Stalnaker 00:35:54 I can ping the Maintainers directly on it.
I think that's a good idea to reach out beyond just the spec typical spec approver books.
For other folks who've commented.
ask, please, Jack C. Joe, Daniel, Josh have all commented, but not approved it yet. So either.
I understand. Like if you don't want to approve it like, if you're kind of like meh, maybe. DM me privately so I'll stop bugging you. If that's the case, I think it's okay to have a couple of people who are like man.
But if there's a lot of people who are, meh? Then that worries me. And we can.
Yeah.
Robert Pająk 00:37:11 Maybe an option will be just if people who are like math just say that they do not see, approve without saying that we don't need this, but we are not opposed to it as well. Something like that. Just to say that the plan is acceptable.
even though it's doesn't feel necessary.
Carlos Alberto Cortez 00:37:32 Yeah, I think this.
Trask Stalnaker 00:37:33 This one is controversial, though in a different angle, though not that people don't need it, but that it. Some folks, at least originally saw this as a breaking change that we should not do because of the impact to the ecosystem.
Robert Pająk 00:37:59 But at the same time regarding the ecosystems, I think all of the backends that were assessed support these right even now.
Ted Young 00:38:07 Right.
But I think that's actually why, like getting maintainers like the other place where this makes changes is at the Api level right? And that is.
Robert Pająk 00:38:17 An SDK.
Ted Young 00:38:18 Project so actually, like reaching out to implementation make maintainers makes a lot of sense for a change like this.
Just to make sure we have not missed a language where this is gonna really screw their game up.
Trask Stalnaker 00:38:31 And one note. When you're reviewing this. remember that this is just an Otep. So this is If we can avoid going into certain nitty, gritty details that we'll get as long as you agree with the kind of broad strokes of the otap versus there's still going to be spec, pr, spec updates to work out, you know, nitty, gritty stuff. And if you want to call those out, that's not a problem. Here we can add those to like the bottom, like future stuff or things to consider. When make sure we include when we're doing the spec Prs themselves.
Carlos Alberto Cortez 00:39:24 By the way, I think the only maintainers I don't see here are the python ones, so probably worth reaching to them directly trust, or I can also write them. But other than that, yes, I think we can.
We can explain more of it.
Yeah, yeah.
Liudmila Molkova 00:39:37 We? We? I have a prototype for python. We discussed it with the python folks. They approved the prototype.
and they are going to. I don't know, alias the the metric attributes, or something to make it type check friendly.
but they are on board with the proposal.
Carlos Alberto Cortez 00:39:57 Yeah, you had totally forgotten about the prototype. Yeah, I review that. Thank you. So I think we're fine on that front.
Trask Stalnaker 00:40:05 But I'll I'll still ping them and try to get some more check marks from them to show on this Pr. That they support that.
Carlos Alberto Cortez 00:40:20 Perfect.
Tyler Benson 00:40:21 I I do have a quick question I haven't fully reviewed the latest of it. But I guess, has. There has the question around backwards. Compatibility been addressed at all like.
for example, sending to different input back ends, like, you know, Jaeger or zipkin, or what it like some some back end that doesn't necessarily have that support for it out of the box.
Trask Stalnaker 00:40:50 Yeah, yeah. Read the Otep. It's all in there.
Tyler Benson 00:40:54 Okay.
Carlos Alberto Cortez 00:40:56 The others.
Trask Stalnaker 00:40:56 Analysis of specific backends.
Tyler Benson 00:41:00 Great.
Carlos Alberto Cortez 00:41:01 Yeah, that one correct.
Okay, thank you. So much for that. Yeah. In that case, I would say, we, yeah, it's up to your trust. But yeah, I think we we are. It's looking good.
Trask Stalnaker 00:41:14 To you. Yep.
Carlos Alberto Cortez 00:41:16 Okay, we have the last item Austin, please.
Austin Parker 00:41:21 Yes, hi, please. Also a side note. Please keep an eye on hotel Maintainers for more info about the great slack brouhaha of 2025.
I was just at the Toc. Meeting. And I'll write that up.
But in hotel news I have attached a link to the document. There's a community issue community Pr, number 28, 1, 7. And I'd appreciate if folks from other Sigs could go and look at the releasemd file and just check it for accuracy. I'm especially curious if there's anyone. Is there anyone from Php on this call.
Bob Strecansky 00:42:20 I'm here.
Austin Parker 00:42:21 Okay, I couldn't find a release Doc or code owners in the Php repos. So if you could go update the Pr and community with relevant information that'd be super
Bob Strecansky 00:42:39 You got.
Austin Parker 00:42:39 Yeah, this is from the Cncf. Doc would like a centralized release document in for graduation, so we could just make sure that the information there is up to date.
Correct, be super.
Bob Strecansky 00:43:02 No sweat.
Daniel Dyla (Dynatrace) 00:43:03 Austin, I I notice you have a like a code. Owners, files linked particularly and contribute those the code owners. Files are not particularly useful.
So we have, like a distributed ownership in Js Contrib. That doesn't use code owners.
Austin Parker 00:43:26 That's right.
Daniel Dyla (Dynatrace) 00:43:26 I. You should make a suggestion on this Pr. To use that file instead.
Austin Parker 00:43:30 Yes, if you have.
Daniel Dyla (Dynatrace) 00:43:33 It is automated or.
Austin Parker 00:43:34 Yeah, that's fine.
Daniel Dyla (Dynatrace) 00:43:35 Some minor automations.
Austin Parker 00:43:37 If there's a different thing for release maintainers than code owners, then please make a suggestion to that thing.
Trask Stalnaker 00:43:48 I wonder, Austin, if the release Maintainers specifically should just link to the like. The read me, Markdown Maintainers Anchor cause code owners also has is more about reviewers. Pr. Reviewers versus release maintainers.
Austin Parker 00:44:13 It should go to whoever it should be, a pointer to the individuals or groups, groups that are able to make a release.
Daniel Dyla (Dynatrace) 00:44:24 Oh, okay, yeah. So our our distributed ownership doesn't apply here anyways, though.
Austin Parker 00:44:29 Right. It's but this is basically asking who has the who has the keys?
I would.
Trask Stalnaker 00:44:37 Probably not linked to code owners for any of the repos. Then because code owners is the list of people who have approval, right? It's not really which is.
Daniel Dyla (Dynatrace) 00:44:51 We're like, I can't please.
I can't release the spec, for example, but I am in the code owners file.
Austin Parker 00:44:59 But the maintainers are also in the code owners. File right.
Ted Young 00:45:05 You.
There's like 2 2 levels here. One level is, I'm trying to figure out who these people are. What are the docs? I go look in to find that out right? And then another level of strictness is having like a link to something that it only contains that information.
And it sounds like you're not asking for the second one, Austin. Right? You're just saying for compliance with Cncf.
Austin Parker 00:45:31 I'm saying, yes, I'm saying like.
what is it? What is the most consistent way we have to communicate?
Where to find the people that have the ability or or have who own the release process.
Trask Stalnaker 00:45:49 Probably I can't have teams.
Jack Berg 00:45:50 Yeah, the Maintainers team for each of these repositories.
Austin Parker 00:45:57 And that is not in the code owners for a repo.
Jack Berg 00:46:01 The way that we structure our teams is code owners. Typically references, approvers and approvers is a superset of maintainers.
Austin Parker 00:46:13 so is it accurate to say, for every repo the Maintainers team for that repo are the release maintainers.
Jack Berg 00:46:21 Yeah. And we have documentation that supports this type of standard arrangement. Right? So in the community repository, it says, these common steps for repository, new repository setup.
Austin Parker 00:46:30 I? Yes, I agree with that, Jack. That was apparently insufficient documentation.
Jack Berg 00:46:37 I? Well, I I also agree with explicitly linking to the individual Maintainer teams. But yeah, like.
Austin Parker 00:46:43 Yeah.
Jack Berg 00:46:43 There's the standard setup. And here are the specific teams for each of the repositories that we want to enumerate.
Austin Parker 00:46:49 That's fine. That's easy enough to change. I'm just pointing out that the desire is the thing we are being graded against is our projects like Kubernetes, or dapper, or whatever that have that release the project as a whole.
And our the way we do it is different. And so it's just trying to like.
Jack Berg 00:47:19 Map it.
Austin Parker 00:47:20 Map map these concepts, yeah.
Jack Berg 00:47:22 Right.
Austin Parker 00:47:23 So I can go ahead. So that that's fine. I'll go ahead and update this to change the release maintainers, to just map one to one to the maintainers of that Sig and drop the code owner stuff. But we do still need a link to like the release docs, or whatever it doesn't necessarily have to be in like release.md. Some people's aren't, or they're like at a different path. That's fine. We don't have to change that I just this just needs to be like a clearing house to go to all of the release docs, Daniel.
Daniel Dyla (Dynatrace) 00:48:00 Yeah, so actually, Trask just posted in the in the chat. I, this link is what I was just about to ask about. I don't believe these links are public, so we should link somewhere public.
I don't think that anybody public can go look at the can like click on a team link and see the membership of that team. So we need to make sure that it's like a markdown file in the community repo, or something like that. I just tried it in a incognito window, and it.
Austin Parker 00:48:33 No.
Daniel Dyla (Dynatrace) 00:48:34 And to log in.
Jack Berg 00:48:35 Yeah. Now, next step would be to try it with a Github set of credentials. That is not part of the hotel organization.
Daniel Dyla (Dynatrace) 00:48:42 Yeah, I don't have a user.
Jack Berg 00:48:44 You don't have that.
Daniel Dyla (Dynatrace) 00:48:45 Saying, we probably should have one to be honest.
Austin Parker 00:48:49 But.
Jack Berg 00:48:51 Hey!
Daniel Dyla (Dynatrace) 00:48:51 May maybe somebody in the security Sig does.
Jack Berg 00:48:54 Hey, Tras? Would the infrastructure as code stuff help with this?
Like, you know, if we have a deterministic place where, like all the maintainers, for all the teams are listed.
Trask Stalnaker 00:49:06 We do?
Austin Parker 00:49:07 Think it would? Yeah.
Trask Stalnaker 00:49:09 That repo is also private.
I'm just checking really quick, because I do have.
Austin Parker 00:49:19 No, I do say I don't know if it's like disqualifying to say like, Oh, you have to be logged into Github.
Daniel Dyla (Dynatrace) 00:49:26 You have to be logged into Github and be an org member, and you may have to have even some greater permission than being an org member. I don't know.
Jack Berg 00:49:40 Sounds like Trask is has a second set of Github credentials. He's gonna try it out.
Trask Stalnaker 00:49:45 Yeah, I you don't need to have any more permissions than an org member. So I did check that. I'm gonna kick my Trask test user out of the org now, and I'll let I'll let Austin know on the on the pr. Now, Austin, do you have a timeline. Do you wanna merge it by end of.
Austin Parker 00:50:08 Rather than later, sooner rather than later is better. But I think I mean.
Daniel Dyla (Dynatrace) 00:50:13 Every repo should have their maintainers documented.
Austin Parker 00:50:17 Yes, every every repo does have that documented in the main. Read me, I believe.
Jack Berg 00:50:24 No, no, some don't.
Austin Parker 00:50:25 Oh, well, never mind f me running then
Jack Berg 00:50:30 And just to just to prove this, go check out the the go repo.
Austin Parker 00:50:36 Oh, well, yeah, you're right. I'm yeah. You're right.
Most repos. Have it documented in the readme.
Jack Berg 00:50:44 I'm not necessarily I'm not. I'm not trying to attack. Go, by the way.
Trask Stalnaker 00:50:48 I know.
Jack Berg 00:50:48 And Lisa.
Trask Stalnaker 00:50:49 Documented and contributing.md.
Jack Berg 00:50:52 Oh, okay. So oh, okay. So it's still.
Austin Parker 00:50:54 I do believe it is listed in a publicly.
Jack Berg 00:50:57 Skeleton.
Austin Parker 00:50:57 For everything. It is also listed on the website.
But it is not listed by.
but it's listed in like a giant like list of just maintainers and not and they're tagged by Sig, or whatever. But it's not one to one mappings.
Daniel Dyla (Dynatrace) 00:51:17 Okay, Trask says it's not accessible without.
So we don't need to get bogged down in exact details here, I just think it's a if we're gonna document something public, we don't want a link that only we can click on.
Trask Stalnaker 00:51:37 I mean, at at least, it is the authoritative link. That's what we.
Daniel Dyla (Dynatrace) 00:51:43 Alright!
Trask Stalnaker 00:51:46 For our ourselves.
Austin Parker 00:51:48 Let me. Okay, let me go. Investigate the requirements. So let me go. Refine the requirements a little more, and ask the Toc, what exactly the goal of this is. Perhaps it is not. Perhaps we can just be like, Hey.
here's the constraints we're working under, what works for y'all.
and we'll figure it out from there.
But, My ask to everyone here is at least scan the release, doc and frequency stuff and make sure that aligns with expectations, slash reality. I believe it is correct, but I am not a hundred percent certain.
And I'll figure out the cut Release Maintainer stuff.
That's all.
Thank you for your cooperation.
Trask Stalnaker 00:52:58 Thanks for yeah, responding to. Yeah, I I agree with you that we're kind of the square and the circle box as far as the Cncf projects go, or like way more distributed unless centralized than other projects. So it's kind of painful to pull this kind of info together.
Austin Parker 00:53:22 Yeah, and I guess while we have a second just to head off. Or if anyone gets questions from maintainers this week, or contributors about chat stuff.
There's no final decision yet on what the Cncf and Kubernetes are gonna do in terms of solutions to the slack thing that'll probably be decided over the next several weeks.
Right now. The priority is getting everything backed up that needs to get backed up. The things that you all should just pay a special note to is, if there are any files that have been uploaded to slack that people use, please make sure to download those and put them somewhere else, because we will. Those will be gone gone.
Jack Berg 00:54:22 Yeah, this is gonna suck I I really have used the you know, the forever history of slack messages. And I I search that heavily to go like find links and reference.
Yeah, conversations with people.
Austin Parker 00:54:39 There, so I will say there is a there. The Cncf. Is getting a complete dump of all public slack history, and will endeavor to figure out a way to make that searchable or migrated even to something else like details. Tbd, there's a lot of like Gdpr and stuff that kind of intercept. There's a lot of like stuff that intersects with that. But they're they're definitely. They definitely have a dump of the history up to this point, and they will be doing another one.
I suspect they will make a decision fairly in fairly short order, in terms of what the next thing is going to be.
But yes, this is very painful to Bob's question about the impetus.
Gotta be money. Yeah.
Daniel Dyla (Dynatrace) 00:55:36 Because they were paying for it.
Austin Parker 00:55:39 So the this, this is like.
So the officially, you know. The only thing that we know is that the Cncf. And Kubernetes were informed of this, there was some discussion.
This was the thing that happened, but also this is apparently happening to other large open source projects on slack right now, it looks like any slack that is on sort of a handshake. Community agreement is kind of getting hit by this. So, for example, Swift, the swift community is also having to deal with this in terms of why, I guess they would like to make more money or stop paying for hosting. All this stuff I don't know. Maybe they need to make the quarter look good.
Daniel Dyla (Dynatrace) 00:56:41 I think, on a positive note. We have done a good job of endeavoring to to get as much important decision making in Github as possible.
For exactly this reason you never know what can happen to recordings or slack messages and all that stuff. So I think in terms of decision making records.
We are not losing as much as we potentially could have.
Had we not been so diligent about that. So.
Austin Parker 00:57:14 I agree.
Daniel Dyla (Dynatrace) 00:57:15 Reminder about why we have that policy.
Austin Parker 00:57:18 Yes, no, I think we're we're we are probably not going to be as hurt by this as some other projects. So yeah.
also, I'm preemptively vetoing Irc, a thing to keep in mind is the Cncf. Does not mandate any particular chat application for projects. We do have the flexibility to do what we want if we so choose from a practical perspective.
I think it's healthy to align ourselves with whatever the ecosystem moves to, just to make it easier for people to kind of like to not have to install 20 different fucking things.
To be quite honest.
discord seems to be, you know, if I was a betting man I would bet on discord for a variety of reasons.
I yeah, I would agree that I think discord is the least bad alternative.
There are things that are better from a sort of moralistic oss perspective regarding like data, governance and whatnot.
But.
Daniel Dyla (Dynatrace) 00:58:43 My biggest problem with discord is that it? It nags end users to pay for like premium discord.
There's no way for the organization to turn that off. I don't think.
Austin Parker 00:58:56 Yes, but also it is that nagging and that individual monetization strategy that makes it less likely to rug, pull the org. So there are, you know, flip sides to these things.
Ted Young 00:59:11 Also we can sell hats.
Austin Parker 00:59:13 We can. We can give out hats. We can give out virtual hats, which would be nice.
Daniel Dyla (Dynatrace) 00:59:18 Very video game focused. But that's probably fine.
Austin Parker 00:59:22 I I not the right venue for this chat, I guess. But yeah, we're not going to do anything in this like extremely short term.
Daniel Dyla (Dynatrace) 00:59:33 Like there will be an evaluation of all these things.
Austin Parker 00:59:37 So, as perhaps may be expected, every single chat app CEO is circling the Cncf. Luminaries like sharks that just smelled blood. So sure it'll be an exciting few weeks for a lot of people that said.
Yeah, looking forward to seeing folks next week in Denver. If you're gonna make it out to that friday is when to to Tyler's Point, Friday. This Friday, the 20th is when the Cncf. Slack goes back to free so on that date you will lose all integrations. You'll lose all. Well, you will lose like web hooks. We'll lose anyone that was using workflows if you're using like the Github app that will be shut off.
We should expect to lose any kind of automation or integrations in slack.
Daniel Dyla (Dynatrace) 01:00:38 Are we using any of them in any official capacity? I don't think we are.
Austin Parker 01:00:42 We are.
Daniel Dyla (Dynatrace) 01:00:43 Oh, great. Okay.
Austin Parker 01:00:45 So we use web hooks. Quite a few repos, or quite a few channels that I've seen use github integration.
Apparently each usage of the Github integration counts as one use. One app. One distinct app is what I'm is my understanding, which is weird. But there are 10 for the entire workspace under the free plan.
So yeah, anyway, that's thanks. All bye, all.
Trask Stalnaker 01:01:20 I.
