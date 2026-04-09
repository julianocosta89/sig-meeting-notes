SIG: JavaScript SIG
Date: 2026-04-08
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 01:04 blue.
**Trent Mick** 01:08 Yo.
**Marc Pichler (Dynatrace)** 01:26 Alright.
And let's get started.
Welcome, everybody. As always, if you have any topics that you would like to discuss, please feel free to just write them down on the agenda here, and then we can talk about it.
First topic I put on here, this is, essentially, just an update.
About the logs API, and SDK GA.
Currently, the milestone is looking pretty good. We don't have… That much stuff left here anymore.
So we're getting closer to finishing that one up.
It's mostly a call to action. If anybody has any, Braking changes, or things that would require braking changes, please, go ahead and open issues, because, that's the… probably the last time we can do it until 3.0 for the SDK, and… I'm not sure if we can ever, make any breaking changes if we add it to the API, so, now's the chance to do that.
And, yeah, proposing that once we're done with the remaining issues, we do another round of spec reviews, just going over things and making sure we cross stuff, off the list if we find any issues, and then we request a review from the TC, and then we hopefully ship it.
as stable.
Yeah, any questions or comments around this?
**Trent Mick** 03:29 Yeah, kinda. So, I was looking at the… one of the remaining issues, the… I'll add a note, so people looking at the issue can know. The… Consider renaming log attributes to complex attributes or something.
**Marc Pichler (Dynatrace)** 03:44 Right.
**Trent Mick** 03:44 I'd be curious for people's… opinion on the name. I'd seen extended attributes used in Python and also in Java, but I wasn't sure what Java's longer-term intentions were there. Java added… so I'll give some color that I understand. Java added extended attributes A long time ago, And I think it possibly before this latest… effort, the latest effort being, like, 6 months ago. I think the cutoff time was sometime in January, was the 6-month period after an OTEP or SPEC change was accepted before they… Something on compatibility that you're allowed to take it out of.
incubating.
But I wasn't sure if Java's long-term intention was to not have a separate extended attributes class or type at all, and just have attributes and roll that in. But I don't know how they do that with their breaking changes.
It's all the breaking changes subtleties are always different between languages.
For us, my running understanding from comments that you've made, Mark, is that we need extended attributes as a separate class or a separate type interface in the API.
Until we do an API V2, because it would be a breaking change.
Python also has an extended attributes, which has an underscore in it. They're only using it for logging stuff right now. I was just speaking with one of the maintainers, happens to work at Elastic, and there's no one currently working on moving that forward.
On the Python side.
Even though maybe it's a little bit surprising, you'd need to talk to some of the other maintainers that are more involved in the AI side, because if anything, one of the motivators for having the extended attributes wider than just in the logging side was to support GenAI semantic conventions that, at least at one point, we're talking about Using… deeply nested.
attributes on spans as an alternative to using log events for… for representing some GenAI stuff, so… Anyway, one… so… one question I have is, what do people think about the name of this new interface that we would have?
Extended attributes is the name I've been using when talking about it, but Mark, I know you always say complex attributes.
**Marc Pichler (Dynatrace)** 06:03 Yeah, it's, I'm also not, deeply, I don't have any deep, ties to the complex attributes name. I just keep using that, because that's what they are in my mind. They're just more complex attributes, so extended sounds fine to me.
**Trent Mick** 06:24 Okay.
**Marc Pichler (Dynatrace)** 06:25 But yeah, I think we would need, a different… a different type, I think, extending the current attributes type is not an option, the way that it is right now.
Because of the subtleties, that… you end up running into when extending a type in TypeScript that way.
**Trent Mick** 06:47 Okay, so, assuming we did that and have everywhere we use the extended attributes type everywhere that attributes… Are accepted in all signals.
Hmm, would we deprecate?
Attributes?
And then, possibly.
**Marc Pichler (Dynatrace)** 07:04 kind of eat.
**Trent Mick** 07:04 of the API, we would just… Have the one attributes type and rename extended attributes to attributes, or… not.
**Marc Pichler (Dynatrace)** 07:13 Yeah, that's a good question. I think… we probably wouldn't want to completely remove it. I'm not sure exactly what the current status is for metrics, if they're still supposed to accept complex or extended attributes, or if they Are not supposed to do that.
Because I think for metrics, the lookup cost could be quite high when paired with extended attributes, especially if you have to recurse into maps and stuff like that to flatten that all out and compare stuff.
So… Not true. I'm still looking again.
**Trent Mick** 08:01 And the OTEP at one point had a thing saying, here, we can bring… that up.
There it says… about, like, the third, fourth, and fifth paragraphs there. OTel API must support complex attributes on spans on blah blah blah, and then the next one is on… may support those other ones, but then the language that's in spec… At that link in chat.
Hmm.
It is basically saying for everywhere, metrics points, resources, instrumentation, scopes.
Is using this attribute collection, which is, in the next paragraph, defined as a map.
to any value.
I'll go re-read on here. But anyway, it's a potential way of a decision point to make there, if we're doing it, yeah. And when I said, would we deprecate it in the API, it would just mean we'd put that at deprecate marker on it. We wouldn't actually… I know we can't remove it.
Literally in the 1.X, so…
**Marc Pichler (Dynatrace)** 09:29 Yeah, one thing that we could do in the future is to… it's a bit tricky to go ahead with this, because, once we have extended attributes and we deprecate the attributes type.
If we ever get to do, API 2.
We probably would want to keep using the attributes name and not extended attributes.
But that's kind of what we would end up with is, attributes dropped.
But extended attributes, still being card debt, and then it would be kind of confusing.
One thing that we could do is, If we ever get to a two of those, still keep both.
And just have… Attributes be a type alias for extended attributes?
**Trent Mick** 10:31 Nope.
**Marc Pichler (Dynatrace)** 10:33 This way… people could still continue using that, and we would probably go ahead and keep using that. So, in that case, we… Wouldn't want to deprecate it, we would just keep it around and let people know that Might change, and then once… Future 2.0 version.
roars around, we would change it, and it would be probably commonly accepted that Braking changes are okay at that point.
And be clear.
**Trent Mick** 11:11 You're saying not deprecate attributes now?
Or, yes, deprecate attributes now.
**Marc Pichler (Dynatrace)** 11:19 I would say not deprecated. But… Add a note on to the attributes type to say that, It might change in a future major version, to the extended attributes type, and strongly encourage people to use extended attributes wherever they use it.
**Trent Mick** 11:47 on.
**Marc Pichler (Dynatrace)** 11:50 I'm not sure if that's the best way to go about it, but it's… We'll see.
**Trent Mick** 11:55 We can discuss it on the PR if I'm coming to get more detail on that. The other question was, Maybe it's just awareness, then. If I wanted to add extended attributes to… the API, that would be in version 1.10, I think is the next one.
Would we be okay making… the logs SDK depend on that version of the API, at least, because Oh, no, sorry.
Yeah, actually. So, if we wanted to… so, okay, this is about coordination of merging. If we're going to stabilize API logs and API SDK and move them into the current stable things.
those things would depend on the new version of the API, because we wouldn't have log attributes defined in… the logs things anymore, we would just have extended attributes.
Defining the API. Okay, so then maybe that's fine, there's nothing really to consider there, other than… the minimum API compatibility is going to jump up.
Which is… might be exciting for people's peer dependencies.
**Marc Pichler (Dynatrace)** 13:03 Yeah, it will jump up at least for, SDK, logs, which is experimental anyway right now, so that that would be, like, the last… the last breaking change would be that we raise the API version, and we would do that within the major bump to 2.0, because we are jumping from 0.200 something to… to doodle directly.
So there's some… Last breaking change there, but, then it should be all good.
**Trent Mick** 13:39 Okay, and then followed swiftly by a… Couple of months later with a 3.X, I guess.
**Marc Pichler (Dynatrace)** 13:46 Yes. As we do.
**Trent Mick** 13:47 Do you do the same for tracing and metrics?
Yeah.
Okay, so.
**Marc Pichler (Dynatrace)** 13:53 Yeah, if we run into any issues that we see from that, we can make some changes in 3.0 then. I hope we don't run into that and everything goes smoothly, but, we see any… any issues that we still want to address once we go GA with the Logs SDK, then we could still make some changes there.
Right.
Give me… other things to talk about here, about the Logs API SDK.
If not… Then, let's move on to the next one.
We briefly talked about the possibility of having an end-user survey, a few weeks ago, I think, and I have been looking into defining some questions And just wanted to ask all of you if there's anything that you would see as a must-have for that survey, or any questions that we should definitely ask.
Anything that comes to mind immediately.
**Marylia Gutierrez** 15:23 So yeah, also, I took a look at the questions that you already added. So, my plan is to have, like, for example, the first set of questions a little more generic, the things that can fit for everybody, so it's not.
**Marc Pichler (Dynatrace)** 15:36 It's like.
**Marylia Gutierrez** 15:36 huge things, like, for example, which, like, language and version are you using on that language? Because I have, like, Java also want to know their version, Python want to know their… so this way I don't have, like, which node version to use, which Java version to use, so it's not like we're.
**Marc Pichler (Dynatrace)** 15:49 Right now?
**Marylia Gutierrez** 15:50 And then after the ones that, like, very specific, then when you can go, like, to the next page kind of thing, I would make, like, the person select the language that they use, and only show up the things that are relevant. But at the same time, I want to make sure that the questions, actually, we can do something with that information, because, for example, I saw a few that you added for, how was your experience, like, using the SDK, like, from 1 to 5.
If they say, like, it was horrible.
what we can do with that information. There's nothing that we can do, because we.
**Marc Pichler (Dynatrace)** 16:22 Yeah.
**Marylia Gutierrez** 16:23 was horrible, so I'm thinking a lot of more, like, sometimes, like, open-ended questions to let them, like, say whatever they want, and a few very specific that we care about as well, but yeah, just to give a little more context as well.
**Marc Pichler (Dynatrace)** 16:40 Yeah, this, this, example that I put here with the, surveys is mostly just a brain dump, nicely formatted by an LLM. So, yeah, I think that's good input. I'll look into, throwing out a few of the things there. It's a bit verbose. I think you're right there.
Yeah, and then probably I can also get rid of some of the other things, like the, first section there, probably can be dropped completely, then I can just focus on Notar.js, related stuff.
I think it's.
**Marylia Gutierrez** 17:21 Yeah, at the same time, if there is generic things that you want to know, yeah, please also let me know, because then I can add to the general. Otherwise, like, all the six will only give me specific, and I don't actually have general questions, but yeah.
**Marc Pichler (Dynatrace)** 17:39 Yes, that sounds good. If anybody has any ideas, please feel free to just comment on the list here as well, and I will try to, roll these comments into the document there. I'm not sure if there's a good way to collaborate on something like that. I haven't looked too deeply into that.
**Marylia Gutierrez** 18:05 Yeah, so far I'm just gathering whatever people send me, I'm putting on a dock.
**Marc Pichler (Dynatrace)** 18:09 God.
**Marylia Gutierrez** 18:10 as is, then I can later on, like, group on things and see what I can turn into a more generic. But yeah, right now it's just also, like, a dump of things that people send me.
**Marc Pichler (Dynatrace)** 18:22 Alright.
**Warre Pessers** 18:31 Yes, that would be my agenda item. I'll introduce myself really quick. I'm one of the maintainers at the Lambda sub-project, so we built the AWS Lambda layers for all the instrumentation. I haven't really been very active on the JS side, but some of you may have seen some of my stuff.
this PR has been open for quite a while. I've put some finishing touches on it, and I'm going to do some small touch-ups still, but I was just wondering if we… can maybe get someone to look into this. I don't know the code owner, if I might be able to reach them, through Slack, because I didn't really seem to find, an account that matches the GitHub user, but yeah, this would be a very nice feature for us to be able to use in Lambda. I've made it spec compliant for now with an experimental, feature added on.
And there is ongoing talks, to update some of the specs as well, but, just like this SIG meeting, the, SEMConf SIG meeting is at a very inconvenient time for me to join, so that's a little… Slower going there.
Yeah, so just wondering, because, I believe Max joined you guys last week, and he also, pinged me about this one again.
Hmm.
So, not sure if there's anything you still want me to… do, Or who to contact to look into this further.
**Marc Pichler (Dynatrace)** 20:28 I wasn't here last week, so I, don't, know exactly what happened, but I can forward you the, person to reach out for.
Who is the code owner? I have a thread this.
**Trent Mick** 20:45 This is Jonathan, that's JJ2 there, right?
**Marc Pichler (Dynatrace)** 20:48 Yeah, Jonathan, the, aye.
Don't… Oh, Ebert, Ebert… send you, their contact on Slack, and then you can, one, reach out to them, and, also, if… they review it, then, once they approve it, that's… that's fine, we'll just merge that in, since Code Online Approver is, is, the same as approver, approver for us in the repo.
And if that doesn't happen, then we'll dig deeper and review the PR there. Might take a bit longer for us to review it, because most of us aren't too deep into The specific instrumentations, but, Yeah, if they don't review it, we'll still get to it. Thank you for updating the, pull requests and, working through the rest of the stuff. I think this has been mostly… waiting for, SEMCOM stuff for a while, so it's, it's good to… when you get the PR merged. I think we have… have had looks, have looked into that, quite a bit, on the car, because we usually do PR triage and go over all the PRs, so having that merged in, would be great.
**Trent Mick** 22:27 Oh, maybe to use some of the time here for a little bit of a debate, I'm just… I just read, The last paragraph.
That you wrote there. How do you pronounce your first name? I don't want to screw it up.
**Warre Pessers** 22:40 You can just say Warren, like, the English version.
**Trent Mick** 22:44 Warren? Okay.
So, yeah, Mark, if you read that for a second, because I bet you're my… you're my opposite on this debate… on this one. I would be okay YOLOing that. Maybe I'm not helping the debate by using the word YOLO, but… If I understand Warren correctly, he's advocating that we go ahead with a change that's gonna remove processing spans, even though the SQS spec still talks about processing spans.
I would be okay with that. My understanding is that processing spans are basically from the Pleistocene era, and don't really belong anymore. What I guess I would take as some comfort for a reason in going ahead of the spec. Anticipated spec work on that is leaning on Warren's appreciation and understanding of what users are experiencing right now, and whether that would be considered a good change for them, or… because technically, that could break some people that are Theoretically. Like, to play devil's advocate to the point that I'm arguing here, right? There could be someone who's used to these processing spans.
And there hasn't been an approved spec change away from that yet, so they would expect to keep seeing that. I don't know.
That's the devil's advocate position.
**Warre Pessers** 24:01 if I can quickly chime in, so… it's taken a lot of time, but if I recall correctly, the normal SQS instrumentation library already doesn't use separate processing spans. The issue is that the… Lambda instrumentation just doesn't have any context propagation as of today. Any context propagation mechanism, sorry.
And thus, when implementing it and adhering to the spec, you, are constrained to… Use processing spans, but the existing Instrumentation doesn't even have them, so… That's also part of why I made that decision.
**Trent Mick** 24:56 Okay.
**Marc Pichler (Dynatrace)** 24:57 Yeah, I think in this case, where… I feel like in this case, it feels kind of clear that the… Lambda spec is just lagging behind, and it's not… intended for it to be that way.
I don't see any… situation where the processing spans would come back in the messaging spec. At least to my understanding, I don't think that would happen.
So in that sense, I… I feel like I'm actually not, taking the diverse advocate stance there, and, I'm on the side of, yodling, as you said, Trent.
**Trent Mick** 25:45 I'm not helping, but yes.
Great!
Okay, I think… I think that helps.
**Marc Pichler (Dynatrace)** 25:56 Especially in the.
**Trent Mick** 25:56 doesn't necessarily mean that we're gonna get a review for you super quickly, Warren, but I'll try.
**Warre Pessers** 26:03 Yeah.
**Trent Mick** 26:04 Yeah, I didn't say everything Marillian, don't put words.
**Warre Pessers** 26:09 Yeah, I'll go ahead and, like, double-check everything, because so much time has passed, and then I'll also contact, Jonathan as soon as I, have his info, but thanks for discussing a little bit also.
I hope we can get this moved forward, in the future, then.
**Marc Pichler (Dynatrace)** 26:31 Yeah, I would, send you… the thing… let's continue on with the meeting for now, and if I don't send it to you, please ping me.
**Warre Pessers** 26:45 Yeah, sure.
**Marc Pichler (Dynatrace)** 26:45 Forget about things, so… That can be helpful.
Alright.
any, questions or comments about, about that specific PR.
If not, then, let's move on to, to bug triage. If any topics come up, or there's any other PR or, something that you would like to talk about, please feel free to, just interrupt me.
During triage, and then we can talk about your topic to make Best possible use of the time.
Are we on the car?
Okay, huh?
The first one here is… Park ticket, that does not look like it's supposed to be a park ticket, but reported through the security, PIP.
**Jamie Danielson** 28:14 I don't remember, did we end up creating a generic ticket for… Like, the sanitization of… database instrumentations.
I don't remember where we left off on that.
Because I think this is probably in a list somewhere of… Things to do at some point.
C…
**Marc Pichler (Dynatrace)** 28:49 Because…
**Jamie Danielson** 28:50 I guess there's a few.
Sanitized DB statements for static queries, yeah, there's, like… There's definitely a couple of them.
**Trent Mick** 29:04 There's not a general meta issue that I see them.
**Jamie Danielson** 29:07 - The closest to a meta-issue is the reviewDB span names for spec compliance.
But it doesn't have a list of things. It's more of one of the bullet points that you mentioned in there is possibly supporting sanitization of the query.
Because we were trying to figure out if we have the names right.
**Trent Mick** 29:34 Right.
**Jamie Danielson** 29:35 But that might be worth creating one. I think we were… Just putting notes somewhere.
I… have no idea where.
**Marc Pichler (Dynatrace)** 29:52 I think for that one… Here, we can probably keep that labored as… Fuck.
And… I don't know.
inclined to put the P1 on there, because, we should definitely synitize that. What do you think?
**Jamie Danielson** 30:27 It's a thing for all of the… like, so someone had put in… a fix for MySQL 2 last year.
So that one's been updated.
**Trent Mick** 30:38 I think this one's an interesting case. Well, I mean, I… okay, I think the meta issue to go through them all to make sure, because it takes a while to get in your head what the rules and the semantic conventions and spec rules are for db.query and db.sum…query.summary, or db.query.txt and .summary, which we don't do summaries and stuff at all, with parametrized or non-parameterized queries, depending on what the database library supports, kind of thing. I think this Redis one's an interesting example in that I'm sure we're probably just Passing the arguments through all the time, but those… those… at least the examples given there are basically an example of parameter I squared, because I think in the… Redis library, I'm guessing you get those as separate arguments instead of, like, one big query string? I don't know, actually.
Do we know?
If they're separate arguments given to the thing, then we should probably definitely be sanitizing them, and just… you don't actually pass through the arguments.
on.
But… Sorry, so, I was disorganized, sorry. I think having the one… Metaissue would be useful to go through.
this one sounds like a bug, I don't know.
P1 didn't, when you had it up there, didn't have the word security in it, but… I don't know. I'm happy to treat it as a P1, if it's a sensitive data.
**Marc Pichler (Dynatrace)** 32:11 I think P1, it's the thing that fits best.
Because… Cause problems, and then…
**Jamie Danielson** 32:22 Jeez.
**Marc Pichler (Dynatrace)** 32:23 Yeah, It's one of these things that shouldn't really end up on an issue, so we don't have a category for it.
**Jamie Danielson** 32:37 I can create a meta issue after this, or in the background.
**Marc Pichler (Dynatrace)** 32:41 Yeah, we can… yeah, we can just use them together.
**Trent Mick** 32:44 works.
**Marc Pichler (Dynatrace)** 32:50 This is in RedisCommon, I think, so it would be affecting both.
Redis and I.O. Redis.
I think that's shared code between the tool.
It would be interesting to see if, actually.
**Trent Mick** 33:15 Of these new commands.
Since the last sentence is used.
Like, config and ACL.
**Marc Pichler (Dynatrace)** 33:32 actually not, too familiar with Redis, so…
**Trent Mick** 33:38 No, those are commands that are in this… I was just looking at this… the Redis common.
library that I need.
Yeah, I don't think there's anything in there about… considering… What that function is, is how many arguments do we expect to see for a given command, because a different command has a different number of arguments.
And then serialize those in… the DB statement.
Alright, db.clear.txt now.
But it doesn't do anything about sanitization, about whether we are worried about those arguments having sensitive data. So, I mean.
for all I know, like.
the set commands, the values that are being set could be sensitive data, so we probably shouldn't be passing those at all. We should just be sanitizing those with a… with a question mark, or whatever syntax we want to use for that. So, yeah.
**Marc Pichler (Dynatrace)** 34:32 I agree.
**Trent Mick** 34:35 People want it back, so we need to opt in.
To get those back, bro.
**Marc Pichler (Dynatrace)** 34:40 I think, yeah.
depends on, what it is, but I think, these, they probably wouldn't unpack.
**Trent Mick** 34:52 Yep.
**Marc Pichler (Dynatrace)** 34:56 Alright, so that's this one here. Anybody wanna work on that one?
Otherwise, I will, have a look at it tomorrow.
But if anybody, wants to look into that, please feel free to… surface on, or… ask, Somebody with access to assign you.
Alright… This one here seems to… B… seems to have been handled last week?
Dear…
**Trent Mick** 35:46 We were waiting for a response from the author.
**Marc Pichler (Dynatrace)** 35:49 We weren't.
**Trent Mick** 35:50 details.
**Marc Pichler (Dynatrace)** 35:54 this… warning here, doesn't always have to be, It doesn't necessarily indicate that there's a memory leak going on.
It… I think the way that it works, it just, logs that when you add 11 Finnish listeners, and we need one of them too close to span, if I recall correctly.
So, if you have 9, or if you have 10 already registered, and then the instrumentation gets loaded, and it adds the 11th one, then you receive that warning.
It's a bit difficult to… Know whether they are actually running into a memory leak or not.
I think the stack trace could be helpful.
And the repro, what are some we have for it in that case. So let's leave that open for a bit now.
Could be an issue, but don't know for sure.
Alright, now going to, PR triage… Let's see which repo has more open PRs right now.
It's the country people. This one here we already talked about, hoping to merge that soon.
10… this one…
**Jamie Danielson** 38:07 This is the one waiting on the, I think, messaging experimental thing. What was the last comment on there?
experimental messaging convention, so I did some of them.
When we were doing, like, the other semantic convention updates, but…
**Marc Pichler (Dynatrace)** 38:33 I think that was… the issue that I opened, and that one got still closed, and didn't have time to… reopen it. I also don't have access to reopen it, so, just have to create a new PR for that.
Wait, that's… Not the right PR. I do have access to reopen that one, because… That's a JS repo.
Webusted.
**Trent Mick** 39:16 I don't wait a second. Ignore the thing that I just posted.
**Marc Pichler (Dynatrace)** 39:26 Yeah, that one.
Was already approved, but didn't get merged.
If anybody wants to pick that up, I'm not sure if I will have time to work on this.
Soon, but if anybody wants to… open the PR again with the same changes, then please feel free and just take the changes that I made and open a new PR.
I'll also write that down again.
to see if I can reopen that, because that would unblock this one here.
Hopefully, waiting on SimConf for it.
Could… we could also just go ahead and introduce that, experimental… SEMConf value.
ourselves, as a third option.
Given that it's already there for GenAI, if we just make the generic, the generic function.
Also respect that.
experimental Flex, and we could also start using it already.
But I'd rather have the spec in place before we do it.
Alright, that's that one.
Alright, discuss the instrumentation support.
It's, like, no reviews from the owners.
I need to, reach out to Amir, anyway, for… some other… Reasons, or, Write that in my notes, hoping maybe we can get this PR.
going elsewhere.
And this one here, I remember that being quite a large PR because of all the, Or the test fires that were added.
There's just some large JSON fires there that are used for testing, which makes this a bit… Unwieldy to review.
**Jamie Danielson** 42:55 One question I have about that, actually.
I feel like we have… we have a test somewhere… for, like, I think testing context propagation that uses a different repo for… Some of the… tests.
stuff. I don't remember if it's, like, example, trace or whatever, but I wonder if that's something we want to consider for something like this, is… keeping, like, mock data elsewhere to use. I haven't looked at this at all to see if it's possible with the way that it's currently being used.
But that might be something.
To think about so we don't, bloat.
The package is here, if we can help it.
**Marc Pichler (Dynatrace)** 43:38 I think that would be helpful. I'm not aware of the, Of this context propagation test that you mentioned.
But it's very likely that I've just never stumbled upon it, because, it's so well hidden.
**Jamie Danielson** 43:58 Oh yeah, the W3C integration test.
**Marc Pichler (Dynatrace)** 44:01 Yes, that's in the core repo, right?
**Jamie Danielson** 44:04 Yeah… So.
**Marc Pichler (Dynatrace)** 44:06 I have seen that one, but I never looked into what it actually does.
**Trent Mick** 44:11 But that's using a separate established.
That suite, right? As opposed to…
**Jamie Danielson** 44:17 Yeah, like, that one's using W3C slash trace context. Like, it wouldn't be exactly the same as this.
But this is, like, cloning another repo to use in the test?
So if there was, like, a similar sort of… idea. I don't… I don't know if it's the right idea or not, just…
**Marc Pichler (Dynatrace)** 44:51 Yeah, I think if we can make that happen somehow, I think that would be… better.
than having the… A bunch of fires here, because eventually they will also get out of date.
**Trent Mick** 45:10 There's some mechanisms in there to update them.
automatically as part of the test run. I mean, like, this is a… isn't this a standard problem with anything that uses a mocking system?
This is using… So… Is the issue here that you want to solve is not have the repo size get big, or you want the PRs to not look as big? I don't know, I'm arguing the other side of this debate.
**Marc Pichler (Dynatrace)** 45:44 That's a good question, maybe a little bit of both.
**Trent Mick** 45:49 Because if you rename those JSON files to .json.bin, then they won't get rendered in the GitHub.
But you just won't see them.
**Marc Pichler (Dynatrace)** 45:55 Yeah.
**Trent Mick** 45:56 it's a better opportunity to get, like, a… what was the… the XV?
Vulnerability pass-through reviews, but yeah.
**Marc Pichler (Dynatrace)** 46:09 Yeah, I guess we could just go ahead and, or so.
merge this in. I'm… Not completely against it, one of the things I usually do when reviewing PRs, I go and I look at the diff, and then I decide whether I want to or not. And this one isn't really helping, but it's mostly a cosmetic issue anyway, because, like, there's a lot of these, mock response.
**Trent Mick** 46:45 That one's…
**Marc Pichler (Dynatrace)** 46:46 Sure, just,
**Trent Mick** 46:47 But…
**Marc Pichler (Dynatrace)** 46:49 The instrumentation changes are also fairly large, but there have been… I have probably opened larger PRs that you had to suffer through, so.
**Trent Mick** 47:05 I mean, yeah, I guess I don't… I don't have a huge problem with the mocks. I'm saying this because I'm pretty comfortable with this test suite, because that was part of writing the… what became this?
And, like, comfort is a big thing on that one. I will say, though, that the OpenAI instrumentation, maybe other Gen AI instrumentations, I'm not sure if the same thing on the Python side, is that they tend to be, like, super wordy, because the GenAI semantic conventions are… The last time I was looking, they were all about lots of discussion from different people to come up with a somewhat generic representation of AI API things that was common between different vendors. So… and getting really structured and really wordy, because there are some efforts to be capturing everything that goes on with chat, request response with an LLM. So… For example, the instrumentation.ts there that had hundreds of lines that were being added, it looks like a lot of that was modeling the structure of things that are being captured, as opposed to, like, you go to a database instrumentation, and they're going to capture, like, four things, right? The query and a couple other attributes about the connection.
These things are capturing ridiculous amounts of stuff, and so… Yeah, I don't know.
Like, another possible pushback is, like, let's test less.
But I don't know how easy that is to… to justify.
Yeah.
**Marc Pichler (Dynatrace)** 48:42 So… One of the things that I'm, wondering now is.
If I understand correctly, you said that these are generated test files, or…
**Trent Mick** 48:56 Yeah, so that's using NOC, which is an HTTP testing library, and so you can set up You, you, what you… It's been a while since I looked at this, but you could set up a… you basically run NOC in different modes. One is to… don't change the mock responses, but test against them, and run a test, and make sure that you get exactly the expected responses. Another one is basically a generate mode, in that I'm adding new tests, and there aren't any test files for the… there aren't any mock expected responses, so it… it will run against a real service, and then write out those files, and then subsequent normal ones, you do that. So that's… this is that generate mode that's going to generate those things. No one's handwriting these things.
**Marc Pichler (Dynatrace)** 49:44 So, because what I'm… I'm thinking of right now is, for Protopath, for example, we don't, We don't.
Commit the generated.
piles.
like, for testing or for, production use. We just generate them.
when we run the tests, and… We could ignore them.
I wonder if that's something that would be possible here.
**Trent Mick** 50:18 These are mocking responses that you would get if you were talking to the real OpenAI service, which… We can't do in testing, because one access to, like, it's a for-pay.
System.
I guess maybe in.
**Marc Pichler (Dynatrace)** 50:33 Right, now, now I understand, yeah.
**Trent Mick** 50:37 The moral equivalent is the AWS SDK stuff, comparison to what the tests are doing.
**Marc Pichler (Dynatrace)** 50:41 Yeah.
**Trent Mick** 50:43 And I think those do have small little mocks, but I think those are using inline in the tests.
Mocking library, where, you say.
I'm gonna set up a server, and the first request it gets to return this JSON payload, and the second request returned this JSON payload. So, similar equivalent, but they're not put out to separate files. And then the question here is the scale, in that… there's this… tendency always to, when you're adding new functionality, add new tests for it, and the test suite's already really big, so I'm not going to go see if any of the existing tests effectively cover the same thing, I'm just gonna add a few more of these. And when you can generate these files, then it becomes really easy to just add new ones, and so they're going to be a zillion, and it'll always grow here.
**Marc Pichler (Dynatrace)** 51:32 Yeah.
Sorry, at first I didn't understand where these files were coming from, but I think I know now. So… my brain is, a bit more fright than usual, this time. So, thanks for walking me through it. I'm… Not completely against.
going ahead with this PR, and many different test files here. So if anybody wants to review that one, and wants to get that merged, I'm… Not going to block it.
This is mostly just, I'm not sure if I'm comfortable reviewing it, this way, but if somebody else does, that's completely fine.
**Trent Mick** 52:32 I feel bad because I'm technically one of the owners of this, because we did the original at work, and then… donated upstream. I'd be happy if Jamie's moving on to doing more.
GenAI stuff, then she could feel responsible for this, but… I haven't been following what's going on in Gen AI SemConf, and it's, like, it's a lot, so that, like, my only real question for this at all would be, does what is is what's been added here following what is agreed, GenAI SamConv.
And does it not have security vulnerability issues in it? Otherwise, it's all good.
I don't have the bandwidth right now to do that.
**Marc Pichler (Dynatrace)** 53:19 Alright, So… I'm wondering… How to go ahead with this one now. Looks like Hector would be…
**Trent Mick** 53:37 Yeah.
**Marc Pichler (Dynatrace)** 53:38 Interested in reviewing that one.
Once we get an approver, would you be okay as an owner if we just merged it in? I'm not sure, I think Hector is not an owner, right?
**Trent Mick** 53:51 Hector's not, no, but, if Hector's cool with it, I'm good.
**Marc Pichler (Dynatrace)** 53:56 Alright, then I guess… We'll see if the person, is interested in picking that back up.
And if there's approval on it, then we merge it, otherwise, we… Close it for now, and see if the person, shows back up at some point.
G.
Let's continue here.
to renovate PR, we can skip that one. I've seen quite a few of these, kit.
conflicts, and then… He left behind.
It's manually fixed, so… So updates these, and then removes a bunch of that stuff.
Probably want a spin-off, an issue to update these, because we should update these at some point.
I'm not sure what's, deal with this one.
Using expect… Things like this one actually just got… Stuck.
So, I just… Check this box and see if it gets unstuck.
**Trent Mick** 56:17 Bill testing question, how many assertion libraries do we have in the repo?
**Marc Pichler (Dynatrace)** 56:21 Mmm… more than I would like.
I think… Usually, we don't add any, additional ones. Some of these, they just were there for quite some time, and nobody removed them. I think they have been here for… Since before I joined the project, even.
**Trent Mick** 56:46 Yeah, I know, that's not a challenge, it's just…
**Marc Pichler (Dynatrace)** 56:49 Yeah, I understand, but it's also one of the things that I usually see the renovate bot updates, and I go, like, at some point, we have to remove them, but… an emergency.
**Trent Mick** 57:02 And then I feel like…
**Marc Pichler (Dynatrace)** 57:03 Forget about it.
**Trent Mick** 57:04 Yeah.
I feel like we're gonna do the SDKv3, and we're, like, almost at the point where, hey, we can drop a whole bunch of old stuff, but do we have the API still lying on to really old versions of Node?
**Marc Pichler (Dynatrace)** 57:20 Yeah.
**Trent Mick** 57:20 That's a… that's a thing to discuss at some point, like… Can we… drop some node versions of API support without… A major version bump? Or do we start doing major version bumps at the API? Boy.
That's gonna be a loaded question. Can't ask that, it's 3 minutes left, so sorry. I didn't ask.
**Marc Pichler (Dynatrace)** 57:44 Yeah, Let's see, maybe it will be possible at some point. I think at least dropping runtime support has been discussed.
In the past.
I'm not sure what the outcome of it was.
But… That's something that kind of blurbs when we get there.
No.
I guess we can end the meeting, at this… For null .
My brain is super fried today, so, won't manage to… Come up with anything good in the last 2 minutes.
Thanks everybody for joining.
Have a nice week, and see you next week.
**Trent Mick** 58:46 Thanks. Thanks, Veron.
**David Luna Bistuer** 58:49 Bye.
