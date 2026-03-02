SIG: PHP SIG
Date: 2025-07-16
Duration: 71 minutes
============================================================

## Zoom Recording Transcript

Cees-Jan Kiewiet 00:03:09 No.
Okay.
Hello.
Sergey 00:03:30 Somebody is drilling hard.
Now I understand why some people can go really crazy with the neighbors like this. Is it? Is it you?
Is it.
Cees-Jan Kiewiet 00:03:41 Is it gone from you?
Can you hear the thrilling Hi!
This is John, is it? Is it coming from you?
Let me check.
Sergey 00:03:56 Yeah, it sounds like, Wow, I hope it doesn't drive you crazy. Okay.
Cees-Jan Kiewiet 00:04:00 Oh, no, no, it works, it's not even drilling. This is one of the aircraft.
so I'll I'll just mute bullet. Don't.
Sergey 00:04:09 That's fine. I mean, I was just just remind me sometimes I hear people that almost murdered their neighbors for this, and I always wondered, can it really get this bad? And it sounds like it can.
Cees-Jan Kiewiet 00:04:22 I barely hear it.
Sergey 00:04:25 Yeah, I guess. Yeah, you can get too used to everything, I guess.
Chris, while we're waiting, I wanted to ask you a small thing. So I looked at the Pr. I was just wondering.
What would you recommend to start? Because maybe I need to 1st understand the background for spi.
Do you guys have some, maybe like a basic thing that you wrote as a kind of intro for developers, or
like, I was just wondering like before I'm start asking questions of the Pr. Itself. Maybe it would be better for me to
to go over some background thing.
Chris Lightfoot-Wild 00:04:59 Ye- yeah I mean.
Sergey 00:05:00 Yeah.
Chris Lightfoot-Wild 00:05:01 I'm happy to discuss that outside of this. If you want, I'll ping.
Sergey 00:05:04 Okay, I will. I will reach out to you on slack. And you guys can can point me to yeah.
Chris Lightfoot-Wild 00:05:08 Or if there's, you know, a time in the agenda to just whack it on there, I'm sure we could discuss it. There.
Sergey 00:05:13 Okay? No. Problem.
Bob Strecansky 00:05:19 Damn!
Chris Lightfoot-Wild 00:05:21 Renewal.
Bob Strecansky 00:06:01 We're waiting on anybody particular.
Brett McBride 00:06:05 No, I don't think so.
Bob Strecansky 00:06:09 So you do
kick us off, Mr. Mcbride.
Brett McBride 00:06:25 Sure, with my agenda items.
Yeah. Just want to draw attention to
the SQL commenter donation. So I think what happened was Google
some time ago dominated SQL commenter code, which is a little bit like context propagation using comments in SQL statements. So that's slowly going through
what has been accepted, but is going through spick and someone's
submitted a pull request, using our Pdo as a like a test bed for how this can work. So I've been doing a bit of
reviewing on that which is interesting because they're
sort of trying to move faster than the spec, or you know to find what what spec or changes might be required for that. So you'll see the the pull request in contribut if anyone's interested to to take a look, but it's it's not well defined yet how it, how it should work, so kind of probably need some eyes over it to make sure it's
being done the correct open telemetry way, and also that we're not sort of creating sort of tech debt for ourselves by accepting
accepting things before you know, before they're ready.
Bob Strecansky 00:07:55 Is there a link for this.
Brett McBride 00:07:58 I will have hold on a second.
Sergey 00:08:01 So you want to start the unit even before the the spec is finalized.
Obvious things to to work on.
By the way, just understand the context. What does it allow to do like? You can pass telemetry information as part of the comment in SQL. Query, or.
Brett McBride 00:08:17 Yeah, that's exactly what it does. Yep. So that if you look at using postgres as an example. You know, there's there's metadata views, anyway, for which queries were run, and you can see in a SQL. Comment either the trace information which you can link back to a open telemetry trace, or I think there's also a fallback to use a a service name. But these are the sorts of things that are, you know.
being discussed. You know what's the appropriate way to do it for and for different databases and.
Sergey 00:08:52 And it somehow can be interpreted on the server side, like server side, can see those comments, and can somehow.
Brett McBride 00:08:58 You know, like.
Sergey 00:08:59 To collect.
Brett McBride 00:08:59 And I.
Sergey 00:09:00 So. So why then send them so? This scale comment will reach the server, or it will stay on the client, and only you can like for trace.
Brett McBride 00:09:09 We'll reach the server will reach the server, and should it should in theory be logged by the server. You know, if if it's logging queries. That's the one well done, Bob.
In that point it seems quite manual, you know. I I looked in some database metadata views and saw a slow query and saw that had a comment, and then
copy and pasted that into a different tool and looked it up. So it's not. It's not
re. It's not real integration with with open telemetry, but it it does do some form of tracking.
And and this and this is why we, I think we need to be careful about this one because
because it's not, it's not. It's not very well defined thing yet.
Chris Lightfoot-Wild 00:10:15 What's not sorry. Go.
Sergey 00:10:18 Let's go ahead. Chris, yeah.
Chris Lightfoot-Wild 00:10:20 Oh, thanks I thought I'd recently seen something, but then I couldn't find it for reference where maybe needed, pointed out something along the lines of
invalidating like query caches. With the randomness of these comments.
Brett McBride 00:10:35 Yes, that's certainly a concern.
Chris Lightfoot-Wild 00:10:36 I think I could find it for reference to this.
Brett McBride 00:10:42 Yeah, yeah, it is a concern. And and these are the sorts of things that are going to to come up. But yes, and and it turns,
you know, a low cardinality semantic convention into a very high cardinality.
semantic convention attribute and yes.
yes, there are. There are curly things that are going to come up.
and and other issues like truncation of of queries, you know, if you put it at the do you put? Do you put the comment in the at the front? Do you put the comment at the end? It might get chopped off. It can interfere with query hints. There are many, many gotchas.
Sergey 00:11:29 So just to clarify. So you're saying it's kind of like not fully integrated with the whole hotel thing. It's about like people
looking for some kind of logs and copy paste and stuff to other tools, and then they can use it so. But you think this is a valid use case, that being of interest to
Ross.
Brett McBride 00:11:47 I mean, it must be. It must be valid because they did build it. So it's based on a Google Google sequel commenter
product which was donated. So it's clearly being used by folks, and they found it interesting or useful enough that
that that at least the code donation was accepted by the opentelemetry org.
I guess I guess it gives at least gives you the capability to correlate
from the database back to a back to a query. Obviously we can do it the other way. We can correlate
by having instrumentation on our database
layer in our Php application. We can track the database calls from the application, but this is going the other direction find which application executed or caused a database query.
Sergey 00:12:48 No, the use cases always seems to be valid. I just assume that there will be other side running on the server, and then also sending complementary information, so you can stitch it all together. But you send it. You're not aware of any automatic agent running on the server and sending the other side of this piece.
Brett McBride 00:13:06 No, no, that would be. That would be very interesting. But that would be a whole new seek in in, you know. Open telemetry for oracle or
Yeah, I've I've not heard of anything like that existing.
Sergey 00:13:24 Okay.
Shawn Maddock 00:13:25 Can we tag it with like waiting on spec or something like that implement until.
Brett McBride 00:13:33 We probably should. I've kind of mentioned in comments, you know. I think this is blocked until we at least figured, you know, X or y out in in spec. But
yes, I think it's a good idea.
Yeah, yeah. And that's that's sort of my concern is that these guys are really running ahead. And I, you know, it's good good that they're enthusiastic. And yeah, but but we're sort of I feel like we're we're the guinea pig for how this works, and I don't want to sort of incur the
the tech debt.
Sergey 00:14:12 And when you say that code is contributed, do you mean this, Pr, or do you mean that there's also some other code that is already contributed.
Brett McBride 00:14:19 There is other code. Yes.
Sergey 00:14:22 Is it like for other languages, or related to application itself.
Brett McBride 00:14:28 So Google, SQL, commenter does have multiple
language implementations. There's Php, I think there was python like, there's maybe 4 or 5
language implementations. And the Php was I think it was just for Laravel.
So it was a bit of yeah. It was a bit of a half baked.
in my opinion. From looking at it.
so that was donated sort of in totality to to
opentelemetry org. But if you were to find the repo. That's kind of being I'll say locked.
I can't remember what they've anyway, they've locked down, saying, Look.
we're not going to use this exactly as it is, but we'll
Thank you, Chris.
But yeah, the the idea is to, I guess. Take some of the concepts from SQL. Commenter and make it more
open. Telemetry centric, and you know, do it properly.
Sergey 00:15:37 Right. The reason I'm asking I understand now. So you're saying essentially, just correct me if I'm wrong, you're saying that the way it exists now is the what is contributed is just a collection of implementations for various clients database clients. I was just wondering like when you said, I thought maybe Google implemented server side, and maybe on their database like a bigquery or whatever. Right? So maybe they had something running on the server side. And this is what allowed them to stitch all together. But you're saying the way it stands now. It's all about the client. There is no server component in this contribution
for download.
Brett McBride 00:16:08 Look, I'm I'm not aware of there being a
a server side component to it. No.
Bob Strecansky 00:16:19 And this was discussed a bunch of times in the Maintainers meeting, and that, like all the people that were
discussing it, we're definitely ex Google people and our current Google people. And they did seem very interested in having this implemented. I can totally see how this could be really helpful, especially in the microservices architecture. But we'll just have time. We just have to.
We have to tread lightly, but I think it is something that a lot of people are
shouldn't say a lot of people, because the Venn diagram people that are trying to know this is close to 0. But it is something people will ask for. I have a strong feeling.
Brett McBride 00:16:53 Hmm.
Sergey 00:16:54 But I'm just trying to do. Do you have a pointer to a use case like, what is the motivating use case? Because the way you describe it, like all the data, is is already there. Right? If we send it to Collector, we can. We can like you what you said, brother you're interested in in reverse mapping, right? You want to go from the query and understand which services use that query right?
You can do it like it's already there, like in Spence. It's just a question of if we'll collector, or whatever other component that you want to implement to. The backend will do that work, but the data is already there. You don't need this additional comment to derive that. Or maybe I'm missing something.
Brett McBride 00:17:30 You can go.
Sergey 00:17:31 From all all over the spans. Right, extract all the queries, and keep the original trace ids, or whatever else you want like. We said. Whatever the cardinality you are interested in, you can still do it right? You can still do that. Processing like the data, is already there. You don't need additional data. That's why I'm trying to understand. What is this comment ads. That was not there before.
Brett McBride 00:17:51 I think it. It adds that other
the other direction is that someone looking, you know, a dba looking in a database
can say this query is problematic. Here's some metadata for it. Someone can go and look it up.
Sergey 00:18:05 So you're saying they are starting from the log database log, and they are looking on the queries there. They're not aware of the spends that are being sent from the client. Is that what you're saying?
Brett McBride 00:18:14 That's that's my understanding. Yeah.
Sergey 00:18:17 Even though with just trace, Id or anything like that, will not be helpful to them without looking at the expense. So they still need to go and look at the spence, even with tracing.
Brett McBride 00:18:25 Food.
Yeah.
Sergey 00:18:26 So it's kind of like them
finicky, the whole use case. But okay, maybe I need to read about it.
Brett McBride 00:18:32 Yeah. And look, maybe maybe it's just the 1st step towards you know the the future where open telemetry does exist in databases. And and we do get the you know the full
Sergey 00:18:46 You know, emitting spans from from databases.
Brett McBride 00:18:50 Maybe.
Sergey 00:18:50 Yeah, but you can like, if you're only interested to see like, for example, what is my top query like what you write and which applications use which query you can already have it from the space, like the additional data that will be possible to do with the with some agent, present or database is, for example, ask questions like, okay, which application takes the most CPU, right or space, or whatever server can inform, like what is overloading database. Then, yeah, you need something being present on that server
and being able to reached out and say, Okay, this is this is the queries that are responsible for CPU. And now let's go and find applications that issued those queries right.
Brett McBride 00:19:28 Yeah.
Sergey 00:19:29 Yep, I think so.
But just having, like top end, like, if you can have it even now, you don't need that additional agent like, if you're just interested in knowing, like, what is the application issues? Like, most, you know, most queries or questions like that.
But yeah, okay.
Bob Strecansky 00:19:45 I. I don't think that this is super helpful, for, like a traditional lamp stack where you just have the like, all of the components. In one place, I think it's
like very helpful when you have distributed, like microservice architectures where many things may use the database and you know communication isn't perfect amongst teams, or whatever I think that that's where this probably really shines. The most.
Sergey 00:20:08 Yeah, I I understand that maybe there there are use cases that I am not aware of. But that would just be interesting to understand like use case end to end right like. If we just send you trace. Id sounds to me that you will still need access to those funds.
But if you already are building on the access to response, then why do you need this additional thing? Then? Just
just use the spans. They have all the information that you need you. You see the query there, and you see, trace id there. But okay.
Brett McBride 00:20:36 Yep, I mean, I yeah, I I agree.
I agree. But some people think it's useful. Clearly.
Sergey 00:20:44 That's why it would be interesting to send the use case. They always maybe come in from, like Bob says, from different point of view of people that come from. Maybe database administrators, or anything like that like that would be interesting to see how how it would be useful to them. Yeah.
Brett McBride 00:20:58 Yeah.
I think I have one other thing on the on the agenda.
Bob Strecansky 00:21:10 You do.
Brett McBride 00:21:11 Oh, yeah, sorry. It was the the semantic conventions we talked about that last week, just to point out that still
sitting waiting for a review.
Bob Strecansky 00:21:24 Okay, I can review this.
Brett McBride 00:21:26 Thank you. If anyone can take a look at that.
Bob Strecansky 00:21:29 On!
Sergey 00:21:33 You mean the change that you described, the one that introduces Unstable, or what was.
Brett McBride 00:21:38 Yeah. Incubated incubating is the term.
Bob Strecansky 00:21:49 All right.
Anyone else have agenda topics before I walk through the your normal workflow.
Sergey 00:22:02 I had a couple of questions regarding this Bi, but again.
only if time is left, and maybe a little bit sorted by.
I will raise it at the end, but maybe I will have.
Bob Strecansky 00:22:12 I think I think we'll have plenty of time for that.
Sergey 00:22:14 Okay.
Bob Strecansky 00:22:16 Let's see, is there anything in the board?
Chris, you wanna talk about this Laravel in progress? Piece.
Chris Lightfoot-Wild 00:22:27 Oh, the yeah, the stuff well, Brett's Brett's left a comment on that. So
yeah, I can. I can modify it like that. But I think with the spi stuff, I guess the concern I had was big.
There's an implementation for symphony config package, and then separately, V. Lucas dot env.
and I can't test both with spi
in a test. But what I kind of artificially did was like, here's a handcrafted provider, and here's some array of values, and you know, to prove it works. But
yeah, I didn't know if there was a suggestion on how we do like an integration test with a different package. And maybe we just don't at the moment. But
Brett McBride 00:23:19 Yeah, it's a good question. It's a yeah. It's a really difficult one to test. You know, without
spinning up a completely different environment that that has exactly what you want.
yeah, we have. I think we do actually have symphony.
Chris Lightfoot-Wild 00:23:38 Config, or whatever package as one of our dependencies. So I could at least
so this bit works. But the other package isn't a dependency.
Brett McBride 00:23:46 Yeah, I reckon I reckon that one would be there coincidentally, because something else is using it.
because we use. We do use a little bit of symphony throughout.
Yeah. But look, let's let's not let perfect test coverage.
You know. Stop, stop. Good code getting through.
you know, there's yeah, yeah. We've got a lot of things that don't have any tests. So you're doing better than some.
Sergey 00:24:17 Can can you just clarify like is the issue that you have 2 potential sources, and one of them is always expressed because it it's employed by SDK. Is that the issue.
Chris Lightfoot-Wild 00:24:29 Well, there's 2 packages that it covers with spi, and we don't have them both.
Sorry.
Yeah, I can't test both aspects of it.
Brett McBride 00:24:42 Yeah, that's actually, that's an interesting point, though Sergey does.
Does symphonies dot inv come along for the ride because of other dependencies? We have, so that it actually is always there.
I don't think so. I don't think we explicitly use their.in package. We use symphony config.
Chris Lightfoot-Wild 00:25:01 Hmm.
Brett McBride 00:25:01 But I don't feel like the dotting thing would be a dependency of that.
Chris Lightfoot-Wild 00:25:07 I think it is in the the config bit, though. Is it the part of it?
But I guess the weird thing would be if you had like. For example, larva uses the V. Lucas, one that V. lucas.in package.
and then they've open time so, and you can. If there's any differences between the dot env.
You might have teed it up for the other.
But you know the other package, and then symphony interprets it differently.
If we're using it. But if if it's only like
variables that we expect to control, you know hotel sort of namespaced ones, then there's probably nothing too exotic in there that that's a problem for.
Brett McBride 00:25:44 Hmm.
Sergey 00:25:47 But what I'm kind of sorry if you already just covered it. But what I'm missing is that so? You you have a hard time trying to automatically test it. But you can test it manually. This use case that you want to test automatically is that the issue.
Chris Lightfoot-Wild 00:26:04 Yeah, you can. You can test it manually and then only like, like Brad said on the the Pr, like the the way the spi stuff works.
It sort of pre generates a file
via compost plugin. So you can't change that order at Runtime, which is why, in the test. I had to do a bunch of stuff before the auto load kicks in and automatically bootstraps everything.
Which was why I'm a bit gnarly.
Sergey 00:26:35 I guess my main concern is that manually does work like it. So it's all about like how to set up that environment automatically. I just was wondering like if it works manually. That that's fine, like Microsoft would be is that
if it's if it's something that is already being done by SDK like. If it already provides config source, it will always be chosen. But the way you describe it, if it worked manually, that's not the case, my concern would have been that it is the case that if the config source that comes with SDK automatically will always overshadow this additional.
The configuration source that the task will never be used. But you're saying it's not the case. It's just it will be used if people want to. It be used. But.
Chris Lightfoot-Wild 00:27:15 Yeah. Didn't.
Sergey 00:27:15 Maybe I will. If I'm interested in deeper diving, deeper, I will reach out to you.
Chris Lightfoot-Wild 00:27:19 Yeah, I think we have to do something very simply. But I I had to do something very atypical to get the test set up in a way where, actually, if I do what Brett suggested, I'll make a a testable spi
provider and then simplify the test a bit, and then that should achieve the same thing.
Brett McBride 00:27:37 Yeah. So so they both work in your testing. It's just hard to test
one or the other, or both, in our single
sort of test environment for for the sort of open telemetry, mono repo. If you spun up a completely different repo and set up the environment to test exactly one or the other. It would be fine we probably just don't want the overhead of having to do that.
Sergey 00:28:06 Yeah, probably. But I wonder why? Yeah, we can discuss it offline. Like, I wonder, why do we need the whole repo like you can set separate application. Maybe you can even fork it, run it like a separate, or run it as a separate. If it's an issue that you already have something loaded in the current process. Maybe you can just fork it as external process and let it completely be isolated and load configuration.
So essentially, if it's a separate directory, self-sufficient environment. And you just load it. And just, you know, acquire like some results that you can test in your
in your in the process that runs the testing framework.
Maybe there are better solutions.
This is how we do integration testing for elasticity. We essentially spawn a separate process for the application. So it's in no way affected but what we have in test, the process that runs the testing framework.
Chris Lightfoot-Wild 00:28:59 It needs a different dependency as well like the packages are different, and it's to regenerate the underlying file. So it'd have to be like
totally separate dependencies, so not not say it couldn't be automated, but I'm sure it'd be complex
or more complex than what I've got.
Brett McBride 00:29:14 Yeah, yeah, yeah, that that's that's that's the crux of it is that it would just be more complex for us to to set up. I think we could. But it's just
yeah.
Sergey 00:29:23 I mean, I wonder? Like, why? I mean, yeah, I guess I missed some details here, but
the fact itself that testing application, like running is completely self-sufficient. That should be exactly what users will do right. They will set up this application. They will use open telemetry.
and they will maybe configure the resources that they want to use like by itself. It should be quite simple.
The additional advantages of that. It will also showcase how how users are supposed to use this feature right.
because it will not be mixed up with with the testing framework. That will be a self sufficient application that just uses this feature. But again, I need to deep dive. Maybe I'm what I'm suggesting is not is not even applicable. Yeah.
Need to better understand.
Bob Strecansky 00:30:09 Nope, Brett, you want to talk about remove event logger.
Brett McBride 00:30:16 I forget no
Bob Strecansky 00:30:18 I forget.
Brett McBride 00:30:20 We don't even know where we got to. There I feel like I did resurrect a pull request.
It's been managed. Look at that.
Bob Strecansky 00:30:31 How about that? You did it? He merged into 2.
Brett McBride 00:30:34 That one along to town.
Bob Strecansky 00:30:36 Okay, sounds good.
Usc implement span suppression strategies. Oh, this is Tobias.
Brett McBride 00:30:49 Yep.
Bob Strecansky 00:30:54 Looks like.
Brett McBride 00:30:55 Not sure.
Bob Strecansky 00:30:55 It's like.
Brett McBride 00:30:56 On!
Bob Strecansky 00:30:59 Yeah, I think I should.
Shawn Maddock 00:31:04 Tobias. Such a slacker.
Brett McBride 00:31:08 Yeah.
Sergey 00:31:09 Is that the feature we discussed sometime in the past of trying to merge spends it essentially
refer to the same logical action.
Brett McBride 00:31:18 Yes, yes, it is that one, Sergey.
Bob Strecansky 00:31:23 Span suppression strategy. That's a lot of S's.
Brett McBride 00:31:27 So those are related, and the the 1st one, the nive one, replaces.
Bob Strecansky 00:31:34 This, one, okay.
Brett McBride 00:31:37 Sorry.
Bob Strecansky 00:31:38 Should I close? Should I close.
Brett McBride 00:31:39 I think this is redundant. Yeah, look like, yeah, let's close it. Yeah.
Bob Strecansky 00:31:43 And then do you want me to just mark this as well for your ticket as well do, or
I don't think we have.
Brett McBride 00:31:48 I think it's already in there that it's a it's an alternative to.
Bob Strecansky 00:31:55 It's good.
Brett McBride 00:31:56 Alternate. Yeah, it's already there at the top.
Bob Strecansky 00:31:59 Cool for me alright, and then
I think I can look at.
Chris Lightfoot-Wild 00:32:11 Sorry I should have. I should have said actually on that Pr that we're discussing of mine. Brett, if I make those changes. Was there anything else that blocking it? Then? Are you happy to
test it? At the next stage also.
Brett McBride 00:32:22 No, it's otherwise. Look good to me.
Chris Lightfoot-Wild 00:32:25 Cool. Alright, I'll I'll try and fix that up and thank you.
Brett McBride 00:32:28 Make the test happy, or make the test such that you're happy with it, and we'll
I think we can. We can move on with it.
Chris Lightfoot-Wild 00:32:36 Yeah, we've got a lot of room today. Thank you.
Bob Strecansky 00:32:43 Sig meeting info.
completely missed that one.
Shawn Maddock 00:32:54 It. I mean, it's in draft. So it
I just need someone to recreate the calendar invite. I assume that was done on like a notel account or something.
Bob Strecansky 00:33:04 Yeah, I think we have to add, I think we have to ask about that. Yeah, we don't have the ability to. I don't have the ability to change, but I think we have to talk to the
DC. Or the Gc. The general Committee. We can reach out. I'll help you reach out to them.
Sergey 00:33:22 Is, is at the link, and stays the same for the zoom.
Bob Strecansky 00:33:27 It should stay the same, for the zoom they use like a very static, seemed like.
Sergey 00:33:33 So update for the meeting will not involve the link. So just other aspects of the meeting.
Bob Strecansky 00:33:39 I think it's just like they're yeah.
So reach control. The only thing that we missed doesn't look like it.
Instrumentation and everything there, you know. Second overflow questions.
No, no, relatively new bugs, Sergey, the floor is yours for Spl.
Sergey 00:34:08 Yeah, I quickly ask. Maybe it will be better sort of the I I started to ask, and Chris, before meeting started. It's essentially I looked a bit at the Pr. As we mentioned the last time.
we would like to integrate a pump, but essentially kind of like remote configuration feature.
Eventually, when we contribute it so it will be more smoothly integrated with the with SDK or with we decide that we integrate those configuration sources. And I looked at the Pr that you guys mentioned Brett and Chris and I had a couple of questions that I just wanted to make sure before I will start adding notes to the Pr. That maybe there is a background information spi that I can read. Maybe that will answer some of the questions.
And yeah, that's essentially
for my. But other than that, I was just wondering, like I looked at the. For example, I looked at the code and the code that we discussed last time the one that explicitly references the environment file, or how we call it configuration file. I saw that in Pr. It's still there. That code. So I was just wondering. Is that code somehow will also kick in at some stage? Or is this just left there
to be removed separately at the
again? Maybe those questions already answered somewhere. That's what I thought. Maybe I need to read.
read about before I'm asking this kind of questions.
Chris Lightfoot-Wild 00:35:37 Think that was because the the new functionality depends on the SDK configuration package, which is separate.
I didn't know if that was one day gonna be ingested into the SDK, to then remove the duplication, because there's like
the existing environment loaders.
If that package is there gets replaced by the conversion, functionality, or so it's fine.
What's what do I know.
Sergey 00:36:03 So this new configuration. So we still have distinction between configuration being used by SDK versus configuration that are used by
other components, just instrumentations, and
those will might be 2 different sources of configuration.
Chris Lightfoot-Wild 00:36:21 I think it's the same configuration. But you do. You want to take the phone.
Brett McBride 00:36:24 Yeah.
there. There are 2
classes that process, the same file to get different information, either the SDK or instrumentation, that kind of treated separately, which I think is an implementation detail.
Sergey 00:36:44 Yeah, putting aside the whole glasses. And I'm just asking from user perspective, like, can they, in fact, rely that they can both use any source of configuration to use to specify both options for SDK or for any other part of open telemetry. That might be technically be considered instrumentation or other exporter that they.
from their point of view, they used. They see them as separate packages, right? So they don't even know. Maybe they're from the same repo. But even.
Brett McBride 00:37:15 8.
Sergey 00:37:16 Dependency on them. They see all of it as separate packages, right exporters, instrumentations.
So I was just wondering. 1st of all, do we still want that? Do we want to have 2 separate, like from users? Point of view. If we don't want that, then maybe then it's just a technical issue, how we implement that I just wanted 1st to answer the question.
Brett McBride 00:37:38 So this is the separation between.
Sergey 00:37:40 SDK and the rest of it.
Brett McBride 00:37:44 Are we? Are we talking about the SDK configuration package that you have to install.
Sergey 00:37:50 No, no, let's put aside this to hold technical.
Brett McBride 00:37:52 Okay. Okay.
Sergey 00:37:52 Just talking about from user perspective. Like, if I want to specify all my options on OP or on 10 file, do I need to care that maybe it's not possible. And some of the options I do need to put in environment variables. So in any file or any source I can use for all the options doesn't matter to me. If the options used by the instrumentation or by SDK,
you're saying.
Brett McBride 00:38:16 But I'm if I possibly not. But I think, broadly speaking, we've got environment which can be
actual environment or.in files, or php, dot any? So that's that's 1 style
of of configuration. And and yes, you can mix and match, you know, an environment variable with a Php dot any setting
or you're using declarative configuration, a Yaml file which
replaces entirely like once, once you've made the decision to use that environment of any kind is not inspected further.
And then I guess we've got the 3rd one which you're working on, which is OP. Amp, and I'm not sure
how the priority works with with OP-amp.
Sergey 00:39:14 Yeah, like, I said, the OP specifies specifically, the priority is higher than any local configuration, the inspect of the OP. It's reference, what you call environment. I guess it might be confusing, because people immediately will start thinking environment variables, so they call it local configuration versus remote.
So remote, comes from this is local. So I guess dot, N file, or whatever other format that is present.
I guess you can discuss. Well, if it's through the local if you put file on Fc, but let's say just for simplification case files, environment variables. They are looking to the local configuration.
Brett McBride 00:39:48 Yep.
Sergey 00:39:49 And then you have this other, which is considered remote and remote, takes precedence over local.
Now, my my question. So you're saying
all the local or whatever. So we do want all the options to be completely independent of the source. Right? So we don't need to maintain separate source for
SDK. And for the rest of it like it would make sense for all of them to use the same source. Now, just a question of technical implementation. If you want to have separate classes or not like you said, it depends on what what spi, how, what it can handle or not right. But our goal is to have all the options right from all the sources. Right.
Brett McBride 00:40:29 Yes, I think so.
Sergey 00:40:32 Okay, okay, so I just want to clear to make.
Shawn Maddock 00:40:35 Unless.
Sergey 00:40:35 So, okay.
Shawn Maddock 00:40:37 Unless you do declarative, and then that eliminates all the other sources.
Brett McBride 00:40:42 It does, and and yes.
the other thing about declarative sorry to cut you off, Sergey, is that it's a lot richer like you can configure a lot more through declarative configuration than than the limited configuration you can do with environment based
by which I mean, you know, the actual environment. php.any.in file? They're all variations on the same thing, and it and it's a a reduced set of things that you can control.
Sergey 00:41:12 Oh, really! But can you give an example like what can you configure via the file? But not.
Chris Lightfoot-Wild 00:41:18 Okay, just
could, I say, sorry in in declarative, you can still reference environment variables. Okay? Which comes from, that's that's all. So it's still configuration from.in server and any etc, but just mixed in in a more structured like Yaml format, with.
Sergey 00:41:35 That's true.
But I wonder like, why is that like? Sounds like you have basis of implementation that should read that configuration.
and it should be transparent to them where they read it from, whether it's a local like environment variables, any file like, why is it possible to set some configuration in this declarative configuration, because the pieces that read that configuration, why should they care where this configuration came from?
Chris Lightfoot-Wild 00:41:59 You do have to explicitly set that upfront to say I'm wanting to use declarative configuration and provide a path to it. I think.
Sergey 00:42:07 Yeah, that makes sense that that's you're talking about from the user perspective. Right? I'm now talking about from perspective of implementer, let's say, instrumentation, or what other piece that wants to use that configuration
they essentially need to read, to call some Api. Tell, tell it, give me this configuration value. With this key.
they should not care where it came from. Right? That's why I'm maybe I misunderstood what Brett, you said, that it's possible to specify more like, I would assume that
it should be possible to specify exactly same amount, no matter what is the source.
because at the end it needs to be read by this implementation implementing piece.
and it should not care where it came from. Can you give an example.
Brett McBride 00:42:45 Okay.
Sergey 00:42:46 You specify.
Brett McBride 00:42:47 Yeah, sure, you can have 2 exporters. You can have 2 tracer providers or one tracer provider with
a batch exporter that sends traces this way. And a simple exporter that does something else. Yeah. So
if because there's just one environment variable
for a thing in environment configuration, you
I guess you lose fidelity in in what you can. What you can set up
Sergey 00:43:20 Everything. This will be corrected.
Brett McBride 00:43:21 At some point, probably 3 years ago. They put a moratorium on new environment variables because they decided they are not sure who the spec committee. Decided there were too many environment variables. So from that point on, we basically have not added any new environment variables and declarative configuration is, I suppose, seen as
if not the successor to environment based configuration, then at least a a a much richer
replace replacement or alternative.
Sergey 00:44:00 I see. Okay, so it sounds like a completely separate piece of the of whatever we have this issue spec special treatment for declarative.
but it sounds that we can, for now put it aside, because if you understood, if I understood you correctly, you're saying this declarative file will have precedence over any other source of configuration the way it works now, and they got in the remote configuration. We need to find out what what's supposed to be the relation
relation between those 2 sources. Right? It's not clear at the moment we need to clarify that. But let's assume that it should also override the O. Pump as well. Then we can just say, okay. If the clarity was specified, then it just completely overrides as highest priority, and that will solve
those use cases, right.
Brett McBride 00:44:44 Yeah. Although, didn't you say OP. Amp is the like, remote configuration is the highest.
Sergey 00:44:52 Yes.
Brett McBride 00:44:52 Okay.
Sergey 00:44:53 But, judging by what you're saying, I always assumed that remote can always supply everything that local can.
But now you're saying no, it's not the case. In some cases local can specify something. So that means that people might want to somehow mix between them. So I need to find out. That's interesting.
Brett McBride 00:45:10 Excuse me.
Sergey 00:45:11 That is.
Brett McBride 00:45:12 Yeah. Well, suppose the important question is, what what can you specify with OP. Amp? Because I look, I'll be honest. I haven't read the OP. Amp. Spec. So.
Sergey 00:45:22 So it leaves it open like it just specifies that the way the transport works.
But it doesn't talk about like it's obviously will depend. We even made up names, right? So we need to provide the keys for the options. So we just gave them, based on the, for example, the way they've been used in other words, even consistent between different languages, the way they currently defined. But yeah. So for example, we have hotel log level. So this was just remove a tail. Just let's call it log level, right?
That makes sense. But so we have options like that, we can. We can make up names like that. But spec itself, or pump doesn't get into it to just specifies that you send this map.
But you are.
It doesn't get into. What are the keys that you should expect being present there?
Yep.
so okay, okay, I I will. So I guess I will just need to get into. So I was just wondering what would be the background for spi. Just better understand? Because essentially my, I guess biggest hurdle was, I'm trying to understand. Is this the way it's implemented? Currently, will it be compatible with our use case for the remote configuration? And we're just wondering.
is there like examples how people should use this new feature like what would be the example? And this is what I meant by the separate application.
So I was just wondering. Maybe there is already. There are already examples, and this one will just somehow integrate with them smoothly. So even though Pr. Itself didn't have examples. But
they're somewhere else.
Brett McBride 00:47:04 That's sick.
Sergey 00:47:04 So it should cover. So this, this link you you mentioned, it should also cover this.
Brett McBride 00:47:08 So so this is like the this is the Uber example of like. This is obviously very contrived. But but this shows all of the different things that you could conceivably
configure, and and it's deliberately, deliberately overcomplicated to exercise every facet of of declarative configuration.
Sergey 00:47:29 Oh, sorry I didn't mean to clarity. I meant spy spi spi! Thing I meant spi.
I'm talking about the Pr. That is, Chris's Pr, that handles the introduction of this capability of loading configuration from right. That's the purpose of the. And we're just wondering, like how we imagine like how people so essentially do they need to enable, though it will automatically be enabled. But they just need to set a pass to this file or to automatically discovered. If it's present
and
it seems maybe I'm wrong. But like I was just wondering, like is other examples with spi that allow people to
to introduce additional sources of
of anything like the configuration, or any other like additional services like, is it? Is it something like you showed configuration file that can be done
by without changing the code just changing the configuration. Or it needs to be done on development like before packaging. I'm just trying to kind of wrap my head around like, what is the flow like? Is it who? Who 1st of all, who is the end user of it? Is it. The the developers developer need to take care of that before they deploy
open telemetry, or they can. They already, after they open the deploy, changed. What telemetry will use. It's its configuration.
Brett McBride 00:48:49 Yeah. Okay, so service provider. I I think I'm starting to understand what you're saying. So yes, Spi can can do that.
and it's it's kind of it's a little bit mysterious to look at how it does that. But but if you were to look at a class well, for example, in in Chris's Pr. You know it. It'll pro
the. I think it's an attribute to say what it it is a service provider, and it provides
this type of.
say, into an interface, it provides a thing that that implements this interface. So in theory, you could
create and register a.
Sergey 00:49:36 The 1st question will be, How.
Brett McBride 00:49:37 Office.
Sergey 00:49:37 How is this even discovered like, is it? Is it somehow enumerated? I guess I need to look at the.
Brett McBride 00:49:43 Part of composer auto loading it. So you yeah, you need to register it somewhere. There's
there's some tricks to it. And Chris jump in. Help me when I get something wrong. But
Sergey 00:50:00 Guys I wanted to ask like, is there like some kind of like information somewhere that can read on the background? Because I understand that the we have a contribution. We use 3rd party implementation for this spi infrastructure. Right? Spi.
Brett McBride 00:50:14 Yes, but it was also written for open telemetry by, you know, one of our contributors. So yeah, we are the primary use case
for this. It's got. It does have its own documentation on Github. But it's fairly minimal. And you really need to look at what, how it's used in open telemetry, I think, to to really understand
how to, you know, ex extend it in in open telemetry.
Sergey 00:50:43 Right. But so, if I understood correctly the motivating exam, a motivating use case for the even introducing this infrastructure for spi, it was the order of floating all kinds of things right? That take dependency on each other, or maybe in in certain directions. Not probably not each other. But
so if you want to control that order, this is what this is best. Essentially, if I understand, you're saying there is a registration phase, and then there will be kind of like binding phase right after the everything is already registered. Is that?
you know, can I read about that like? What is the stages like? How is it even working? What would you advise for me to get? Look at to in order to understand, like.
what are the stages in this resolution process like you said registering, and maybe other.
Is that what would be the best like to read the code or.
Brett McBride 00:51:33 It probably is. Yeah.
Sergey 00:51:35 I completely want to approach it practically right. There is no like, I just want to to gain this knowledge and help you guys with, and make sure that is compatible with what I want to introduce there what we want to introduce the feature right? So if it's really.
Brett McBride 00:51:50 End, the call.
Sergey 00:51:51 Then I'm fine with it. So okay, no, no problem. I just.
Brett McBride 00:51:54 Look. And I'm I'm obviously happy to help you to the extent that I understood
standard. So we can. We can take this.
Sergey 00:52:00 Yeah, sounds good. So I will. I will start to maybe.
Brett McBride 00:52:02 Yeah, so.
Sergey 00:52:03 You're okay with me posting, maybe some questions that already answered in the past, and you can just point me
on the slack.
Brett McBride 00:52:09 Yes, because I probably weren't answered in the past that were discovered by by us.
Sergey 00:52:15 Fine. No problem. I will start going over the Christmas Pr. And then I will ask questions before I post notes. But yeah, I just wanted to get knowledge and then
participate and help your other guys.
Chris Lightfoot-Wild 00:52:25 I volunteer. I don't want to step on toes, but I don't mind jumping into like a huddle or something with Sergey, and just.
Given a crash course on what I understand of it.
Sergey 00:52:36 Yeah, that might be helpful. Yeah, I will reach out to you on slack. And yeah, if you guys have time, obviously quickly interacting in sync mode obviously will will better. But it depends on your availability. Yeah, let's let's yeah. We'll probably post if there will be meeting. If other people are interested in joining and following it. Yeah, it might be.
Bob Strecansky 00:52:55 We could also just use. We could also just use this time next week to do that. If that's not too late.
Brett McBride 00:53:01 Yep.
Sergey 00:53:02 Yeah, I don't know if you guys want to hold that.
Bob Strecansky 00:53:06 Yeah, I was.
Sergey 00:53:06 Are until the next week. But
yeah, it might also work.
Brett McBride 00:53:12 And it might.
Sergey 00:53:13 We can merge it, and we can always make amends if we drive the conclusion that they're necessary.
Brett McBride 00:53:19 Yeah, if if we had some code to look at. You know, I think we
no, no, yeah, exactly. But if I if I decide what you're going. That's why I didn't want it to to be in this meeting, because this meeting has a clear purpose right.
Sergey 00:53:32 Start going walks here.
Bob Strecansky 00:53:35 We can definitely change the purpose of this meeting once or twice. I think that that might like it. It will definitely benefit.
Sergey 00:53:40 Yeah, whatever works for people I'm fine with, either way. Yeah.
Shawn Maddock 00:53:44 Yeah, I'd love to hear about and just be a fly on the wall during that.
Bob Strecansky 00:53:48 Alright, and that's and that's our plan.
Brett McBride 00:53:50 More people to know. Yes.
Bob Strecansky 00:53:52 That's our plan that next week we'll just walk through this implementation.
Brett McBride 00:53:56 Hmm! Alright! I'm happy with that.
Bob Strecansky 00:53:59 Shake it up a little bit. You know. New open telemetry meetings.
Brett McBride 00:54:03 Yeah.
Shawn Maddock 00:54:06 Being agile.
Bob Strecansky 00:54:08 Yes, we are ready for a new sprint.
Sergey 00:54:13 Just for me to let. Can you please share just for me to? Before that? I guess I don't know. Maybe we'll start since we have a little bit of time, so we can already do it. Now, I just wanted to maybe ask which areas of the code you guys would advise me to look at so can I share. Please.
Bob Strecansky 00:54:29 Yeah.
Sergey 00:54:30 I don't know if you need to release some kind of
Thank you.
Bob Strecansky 00:54:33 So essentially, I'm looking at the can you guys see my screen? I will make it sure it's bigger.
Sergey 00:54:41 So essentially so. This is kind of like, identified it as kind of like the interesting entry point right? Because it explicitly mentions this service loader with the with the resolve, and I assume that this is where the data essentially will integrate right the the tone resolver.
So for me to understand. But I couldn't find like, okay, how do I introduce additional? Let's say, for example, my goal is to understand if I have one more thing like that on the dot env resolver.
Let's call it dot N. 2, and I also want to put it as as kind of like in the sequence, maybe higher or lower as dot N. Or maybe at this point, it's not.
It's maybe it's it's impossible to give to put multiple. So let's just say I have a alternative. One. Right? Let's say dot, N. And 2, and I will want to set it instead of that is part of this. Pr, like, what would you advise me like? Which code would be the best place to start looking?
How it can. So obviously, that means like, I can see what are the classes that implement? Right? And I assume this is the new one that implements this dot right.
Chris Lightfoot-Wild 00:55:58 That's it.
Sergey 00:55:59 Excuse me.
Chris Lightfoot-Wild 00:56:00 No, I think this this looks like I don't know if you're on the same page as well I was maybe thinking about. But in the past, I think neither advised
on an interface. You have a waiting aspect to it, so that you can actually determine the order that these things should load currently doesn't do that. And the the expect. The expectation in this pr, I guess, was that you'd have one of these 2 things
available. But actually, you wanna you wanna leapfrog those to the front for OP. Amp.
so you need the highest or lowest weight, whichever way we, you know, decide
Sergey 00:56:33 We're getting about the way. Yeah, I understand. Yeah, there is additional consideration about the priority. But just considering that I understand that this will have a priority over the or you said it will just replace them because it contains them inside like this is what they comment on the Pr itself.
But let's say, if I want to stay completely in the same, the same kind of like paradigm, and I just want to have a different source. That will also do that right. It was incorporate this and then I and I and it will obviously then inside of it will decide on the priorities right between them. I'm just wondering like. But just by looking where this new implementation of this interface is mentioned.
it's not like 100 clear to me. Okay, then how is it? Even like because it it is mentioned. But I it's not clear like, why, it's even picked up right as a
so I guess because of this right, it has this configuration here.
So it's part of the composer. So that comes with.
Brett McBride 00:57:30 That's a result of it. That's, I think, a different interface. So if you go back to the code, you were at the very first, st when you 1st came in that provider.
Sergey 00:57:41 Yeah, yeah. So yep. And then you looked at the usages for that.
for for the resolver interface this one.
Brett McBride 00:57:49 Resolver interface. Yep.
Sergey 00:57:51 When you, you say, well, not only implementation, but any usages at all.
Brett McBride 00:57:56 Not that what we had there was fine because you had the Php. Any resolver
was the 1st thing that came up, or second. Yep, let's have a look at that.
Okay? So somewhere on there.
Sergey 00:58:12 But this is one of the implementations I was just interested to find, like, how this imp new implementation, this one. Why is it even big being picked up right? So it sounds like it's been picked up because of mentioned it mentioned here
in this file, right? Right? Or.
Brett McBride 00:58:28 It is. Yep.
Chris Lightfoot-Wild 00:58:30 Yes.
Sergey 00:58:32 Got it got it. So that means that if I want to implement a new one.
but I obviously don't have access
to Sdks composer. Json. Right? I'm as a user. I want to add it after I already took dependency on SDK,
so that yep question is, how do I do that?
Brett McBride 00:58:49 Because because all these extra spi things get merged.
And so so I mentioned it in my the key pieces that you.
Sergey 00:59:00 Composer, Jason, I can use this.
Brett McBride 00:59:02 Your application can add more spi dependencies there and then. When you do composer auto load, it runs a post auto like a dump auto load script
which you will be able to have a look at in spi. But but in essence, what that does is merge
all of the configurations from all of the packages that we're using. Combine all of these extra spi bits together and then run through it and generate, pre generate a class map to a file which lives in the composer, namespace in your vendor directory.
which has all of these mapped, and that's what is looked at when you call service loader.
Sergey 00:59:47 Got it. Can can you please clarify? Sorry I missed. I think you just said it, but sorry.
Brett McBride 00:59:51 Mr.
Sergey 00:59:52 You said, when is this? When is this being done? This traversal and generation of the of everything
down on the.
Brett McBride 01:00:00 Script.
So so when you do composer, update.
it updates all your dependencies, and then it runs scripts. And it's it's a it is a spi provides a script that that does this.
So it's all.
It's a plugin, a composer. Plugin.
Sergey 01:00:21 Okay. So if I install compose, if I install open telemetry SDK, as a as a user, right? I put dependency on it in my composer my application.
I don't need to mention any of that. Any of those scripts. They will come from the SDK. Itself, and they will run, including my additions to my additional spi spi sections that I have in my composer
occasion of the polls are Jason right?
Brett McBride 01:00:47 Yes.
Shawn Maddock 01:00:49 Logan.
Chris Lightfoot-Wild 01:00:50 Yeah, that that was right.
Brett McBride 01:00:51 Do have to approve the Plugin. Yes.
Sergey 01:00:54 The Plugin comes from this composer, Jason, like there is. Is it mentioned here somewhere?
Brett McBride 01:00:59 No, the plugin comes from spi, but when you install it, composer will usually say, Do you wish to allow Spi to run.
Sergey 01:01:08 Got it so.
Brett McBride 01:01:09 Okay. It's.
Cees-Jan Kiewiet 01:01:10 So and and like, if you run that, if you say yes, it will update. You compose to Jason to remember that for the next time in your project.
Brett McBride 01:01:18 Yep.
Sergey 01:01:20 Okay, okay, okay, Ricky. So so that means that it's better. So, okay, I guess.
Chris Lightfoot-Wild 01:01:31 If that if that helps, it runs without the Plugin. But then we end up in the same race conditions as what we had before spo was introduced.
Yeah, but on the autoload order things might be registered differently.
Sergey 01:01:46 Yeah, no, I understand, it sounds like this use cases will will cover the. I just need one to to think, then, how we because, currently, as you know, we kind of like install your site, we don't install your application. So that means that we need to find a way somehow integrate in this process without even mentioning
this section in the
in the applications composer Json. So it would be nice if we had some kind of a Api way. So we can kind of like register via the Api. And maybe there is. That's what I want to invest. Investigate, like, if we can register these pieces via the Api instead of configuration file.
That might be, then the the good route for us to that.
Chris Lightfoot-Wild 01:02:33 And I think you have a global vendor package. Sorry, Thereshan.
Sergey 01:02:37 Excuse me. Yeah.
Chris Lightfoot-Wild 01:02:38 You have a global vendor package. Is that what you mean? Sorry? And then rather.
Sergey 01:02:42 We will install one. We'll install SDK as per site, and then we will automatically inject it into the application. So application don't need to take dependency on SDK,
so applications don't need to change. So the use case is
to make what they call 0 code instrumentations. You don't need to change your application. You don't need to be aware of open telemetry when you build your application right? So it's more for devops. Use case.
You sold application the way developers built it. If they integrated open telemetry fine, it will work. But if they are not aware open telemetry, we won't be able to
apply open telemetry automatically, just because of telemetry, is installed on that site.
Not because developers for the application.
We're aware of it.
But
that's the essentially the use case that I'm trying to think. I assume. Maybe again, this file is being read, just a question of if there exists Api that can be called where we can integrate.
that's why I will need to investigate. But
you you guys don't know if there is one.
Shawn Maddock 01:03:47 I mean, I think all of composer
has public Api, like all of its functionality.
So you should be able to trigger the Plugin just by using composers.
Api.
Sergey 01:03:59 No Plugin will run, I assume. Are you saying Plugin will run because the way we install, so we will load vendor with the Plugin. So we we are the sales vendor the way we package the SDK open limited. SDK, right? We bring it as part of the
this per site installation, and we call the auto load of the composer right? And if we agree to the Plugin, then that means that composer will also run that Plugin. So the issue of the Plugin is not an issue. So you're saying we could have mentioned that in our per site installation composer Json.
So we we can take this with our additional, this new class, and put it in our, even though it's not composer. Json belongs to application. But it's still valid composer, Jason, that belongs to this distribution. Let's call it okay. That might also work. Okay.
Chris Lightfoot-Wild 01:04:51 If if we have the weight into the what that SDK configuration resolver does, you could have the site level thing where it loads from. However, you determine, you know, if it's per application install, and you can modify the the path for the
because at the moment it just assumes the install path that comes out of it. Its composer.
install. But you've obviously got a slightly different.
Sergey 01:05:15 It's up, though.
Yeah, that's a different issue. That will would be interesting to find to think how we can resolve. Yeah. But
Chris Lightfoot-Wild 01:05:24 I think that would be possible. So I could. I could tweak this in prep for that if you think it's worth it.
Brett McBride 01:05:32 Yeah, yeah, but.
Sergey 01:05:33 And you think, please go ahead.
Brett McBride 01:05:36 I was. Gonna say, we've also got some prior art for something I can't remember offhand what, but that uses spi and applies on top of it. Sort of, you know, preferences or an order priority, so that
spio run things in, you know, in, in in the order that you can provide some control over.
but we can do that as well.
Sergey 01:06:01 You mean, you can specify order between these 2 implementations of this?
which order do you mean to order between these 2 implementations that implement. The same interface.
Brett McBride 01:06:12 Yes.
Sergey 01:06:13 And okay, that's fine. Okay, yeah,
But I guess. Okay, that's
okay, yeah, that would be interesting
but the way it stands now, I guess it should not have. So if I understand correctly the way it stands now, this implementation includes. So it's essentially
just because it stands above them.
It's kind of like we'll always over shade, do them. So if I understand correctly this at least I don't know if if is this a assumption, or it doesn't necessarily need to do that like. So the current implementation that will be loaded from here by by this class
it it also includes these 2 inside of it.
Brett McBride 01:07:02 Think not, and I'd I'd look at that service later as like an extension point. We may not provide anything yet
that that implements that
And I'd say if we had priority or something, then environment resolve and Php resolver could be bundled into that service loader load call, and you know the order massaged. However, we wish but yeah, I.
Sergey 01:07:32 I think you need to be careful about that, because when you talk about priority, you eventually you only want to load one of those service right based on priority. But here you want to load all of them. You just want to allow each one of them run in turn. If the one with high priority gave up. Right? So essentially, you say, Okay, I will give the 1st chance to the top one. But if it doesn't have the answer. Then I will get get the second chance to the second one. Right to answer that, to give me for that key. Give me configuration.
Chris Lightfoot-Wild 01:08:00 This does that already. If you scroll down a little bit, it should be like a.
Sergey 01:08:03 Yeah, exactly. But that's why that's why I wondered, like your comment when you said that.
That's fine. I'm loading it in this sequence. But this one which will be loaded in this case. This will load this class right if we have it the way it is now specified in the composer Json, and this one still goes and includes those 2 inside of it. That's why I was wondering why is it necessary if this is already exist here, and they will be queried by this order. Right? And this is the order we want.
Why, then, we need to include these 2 inside here.
Chris Lightfoot-Wild 01:08:39 Well.
at the moment that's separated to the SDK configuration. I think that was the ideal. Well, in my head at least, maybe removing the 1st 2 that we have pre existing, because this is.
Sergey 01:08:52 We need to better understand this concern that you voiced.
So we have this as separate package.
Chris Lightfoot-Wild 01:08:58 Yeah.
And then one day, maybe we can unify. I don't know.
Sergey 01:09:03 To be decided, I guess I see. So this one. This class belongs to this package.
Also this.
Chris Lightfoot-Wild 01:09:14 Yeah.
Sergey 01:09:15 And this kind of like a lower layer. So this one is
like, if we talk about dependencies, this one is lower lail a that was in the SDK,
follow Y. So you still have the references to these 2 sources here, so dependencies already exist.
So you also add in dependency here.
Chris Lightfoot-Wild 01:09:38 We also want to.
Sergey 01:09:39 2 ones.
Chris Lightfoot-Wild 01:09:40 Yeah, those ones, those ones are different.
slightly different. They were parted across from ebay's
configuration, for the implementation is slightly different, and
maybe a separate pr, though I think.
Sergey 01:09:57 Okay. So although this one seems to be the same. But you're saying, maybe this one is different.
No, this one is also different.
Okay, interesting, I see. So there may be difference between them. Names similar. But different. Okay.
okay, yeah. So I guess I will start thinking how we can possibly integrate, and then we can maybe have additional may. If I have questions, I will. I will raise them on slack. But I think you. Thank you. You gave me a good test.
a starting point to start thinking about it. Yeah.
okay, have a look at the Pr as well try to.
Chris Lightfoot-Wild 01:10:30 I guess we could still put this in the agenda for next week. But we need to start quite low level with what Spi does, I guess
so we'll answer them.
Sergey 01:10:39 Yeah, I'll I'll probably start with that. Thank you. Okay, that's it for me.
Bob Strecansky 01:10:47 A new groundbreaking moment
8 min past the hour. We've never gone this long in this meeting before. In the 5 years that I've maintained this project.
Ray. Good work, everyone. Thanks for sharing.
Chris Lightfoot-Wild 01:10:59 Enjoying. We'll catch you all next time.
Brett McBride 01:11:02 Everyone, bye.
Chris Lightfoot-Wild 01:11:03 All right.
