SIG: RPC Sem Conv Stability SIG
Date: 2025-09-17
Duration: 46 minutes
Zoom Recording URL: https://zoom.us/rec/share/asKjvNmEr1bBhMZjaHARB4AxGrhRyN_UFVg2QaTK0xVUhQisNLKzA762WfUrQT0q.xSnqCVvot52yvB-2
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 02:56 Hey, folks…
**Steve Rao** 03:02 Uncle.
Yeah, hello, Chaska.
**Trask Stalnaker** 03:34 Ayy.
Just kicking out Andrew's noteetaker.
Goodbye.
**Steve Rao** 03:57 Yeah, today Kevin can, join us, because he, he don't feel very well. He needs to go to the hospital, yeah, this morning.
**Trask Stalnaker** 04:12 I'm not sure if Vanilla's joining. I know she's traveling this week.
So, may just be a…
Alright, let's go to the project board.
And… So we've got, let's see, we've got a few in progress.
Let's see if… does that capture all of them? Did we mark all of them?
**Steve Rao** 05:44 Yeah, are you sharing the sequel?
**Trask Stalnaker** 05:47 I'm not, thank you.
Okay, so let's add this to our PCE…
This one is… So, yeah, I think this one is…
How can I see the project here?
Let's see, this one's not in our project. Let's add that.
That one, I'm not sure… And… I think this one we do have…
Well, I guess I should check…
Was this… did we have an issue?
Rewrite to cover, okay, got it.
**James Thompson** 07:17 Yeah, because that issue's been split into one PR per technology.
if you link it direct… the issues directly to the PRs, as soon as one gets closed, it closes the issue.
**Trask Stalnaker** 07:32 Yeah, yeah.
Alright, so it looks like two of them are in ready to review.
So, why don't we take a few minutes here?
Let's see… okay… Okay, Lydmilla provided some feedback today, great.
adds attributes to each RPC metric via group.
Let me text…
And so… let's look at what…
So if we look, the main change is going to be RBC metrics here.
And so, let's compare…
Okay, so over here we have…
Each metric has its attributes, right? And we have this huge page, yes, which is what we want.
On this one, right, didn't have that. It had… Attributes down here. Okay.
Good, and let's see, so we've got… RPC system… Looks like…
Oh, I see, error type was added, yes, that makes sense. Probably worth calling out in the description.
**James Thompson** 09:52 Oh.
**Trask Stalnaker** 09:53 Network transport… So network type was removed.
**James Thompson** 10:02 Yes.
**Trask Stalnaker** 10:03 RPC method of your service.
Okay.
Great, so let's just make that, Clearer in the description.
So, okay, cool, so you have the network type has been removed…
Okay, and… What does… what does this mean, AWS SDK?
No longer uses.
**James Thompson** 10:53 But can you change the first instance of brief to note?
Alright, you met.
Change that to notes, right? So… the RPC…
service and method, right? So, if you have a look at the AWS page that I've changed.
**Trask Stalnaker** 11:16 Right, which would not be under here. AWS, metrics?
**James Thompson** 11:21 No, it would be either S3 or DynamoDB.
**Trask Stalnaker** 11:30 Okay, let's go to Files Changed.
Nervous SDK, okay.
**James Thompson** 11:41 Yep.
**Trask Stalnaker** 11:44 Did this… Is this connected to… does this need to be in the same PR as the…
**James Thompson** 11:52 Body.
**Trask Stalnaker** 11:53 pans.
**James Thompson** 11:54 So, the description… the note was being updated anyway.
Alright?
So, rather than having the note updated and then removed, Right?
Because the note was… the note got shortened because the description, the brief, What changed?
**Trask Stalnaker** 12:19 The note… Got… oh, so you also… let me look at the… so RPC… Metric CAML, okay.
**James Thompson** 12:32 Look at the registry.
I think that's what changed.
**Trask Stalnaker** 12:36 Okay.
**James Thompson** 12:39 So the Knicks fell down.
**Trask Stalnaker** 12:42 This one?
**James Thompson** 12:43 Yep.
**Trask Stalnaker** 12:44 Okay.
Does… I mean, does this need… like, it… Is this connected to the… YAML…
like, I feel like, like, what I was kind of expecting was just…
just a simple PR that just…
does the attributes, kind of how you did in RPC Metrics.
**James Thompson** 13:14 Yep. Alright, so the problem… the problem we would have is… if I…
With the current standing, the note that came across, the brief, Right?
this… Alright, so if you have a look at the registry and look at the brief for those attributes.
**Trask Stalnaker** 13:36 Oh, the at… oh, because… let me see… because the freeform text…
Was this freeform text before here?
**James Thompson** 13:49 No, but it mentions span. Alright, this matches the SPAN name.
**Trask Stalnaker** 13:58 Let's see… Okay, but this was in YAML, right?
**James Thompson** 14:03 Yes. Alright, but because we're actually putting it on metrics now, it doesn't make sense to say.
For the matching, it matches the part in the span name.
**Trask Stalnaker** 14:15 Yeah, but I mean, it's already there, right?
**James Thompson** 14:18 But we…
**Trask Stalnaker** 14:19 No harm in rearranging it first, and then… Sending an update.
**James Thompson** 14:28 It just felt odd. Reading a dedicated metrics definition and saying, why is it talking about span?
**Trask Stalnaker** 14:36 Yeah, but it's already there. I mean, it already says spam. I'm not disagreeing that we shouldn't fix it.
But it's just…
like, there… when there are a lot of extra changes, it makes it harder to be like, oh yeah, that just moved the YAML in.
No other changes, click, merge.
**James Thompson** 14:59 Yeah, but that's what I originally had. I originally had literally just copy-paste, right, without any changes of wording or any of that, and then the feedback I've been getting is, we should be correcting things as we're seeing them.
Right.
**Trask Stalnaker** 15:19 How about just open the issue when you see a issue there, and then, I mean, and then not trying to put multiple things all together.
**James Thompson** 15:31 Yeah, that's what I originally had.
**Trask Stalnaker** 15:35 Okay, so if we go back to this PR…
**James Thompson** 15:41 I originally had just adding the tables, and I'm like… then I'm told, I'll remove this attribute, add this attribute.
Right? If you see a problem, just fix it. Right?
**Trask Stalnaker** 15:54 Okay, well, I guess I can't speak to that since Lyudmila's not here, so… Maybe we'll just…
Need to take that up.
Again, next week.
So let's look at your…
I mean, so if somebody, like, Linmilla provided specific suggestion.
I would generally just implement that, but not then Come up with other things?
just… accept the maintainer's suggestion and implement that, but not… I think it looks like you then added
A bunch of additional stuff as well.
**James Thompson** 17:20 Yeah, but I was asked to review the content as part of this.
**Trask Stalnaker** 17:28 Okay.
**James Thompson** 17:29 We shouldn't just bring it across as is, we should actually be checking that it's accurate, for accuracy. That's what the comment was.
**Trask Stalnaker** 17:37 Okay.
Then I will just let Linmilla continue. Looks like she's reviewing it already, so…
We should be covered there.
Let's see, the other one…
is JSON RPC span definitions.
Okay, so we had a page for JSON RPC already.
We did not have… Rpc system… For it.
In terms of… Ordering… I wonder…
if it… I mean, it's not a big deal, but… If we,
Rename RPC System to RPC System Name.
But it's fine, it can… There's a separate issue for that.
Yeah.
No, I meant, like, we don't necessarily need it on the old one.
But it doesn't harm it.
**James Thompson** 19:19 I would argue we do…
We do need it on the old one, because we want people to be able to…
have the old def… go to the historical version, looking at the tags, because with the stability note coming in, we're saying, if you're on before this version, so we should actually have what that version was.
**Trask Stalnaker** 19:41 Yeah, but we've already missed that version, because that version is gonna be the one that was… Previously published.
**James Thompson** 19:49 wouldn't the stability version be the next one? Because…
This is still within the same.
Right, there's no breaking changes… yet.
**Trask Stalnaker** 20:01 Well, it depends, yeah. If we… the… the idea was, once this…
project starts, that we would start merging and breaking changes, and…
But if we don't, then, yeah, if it happens to… Workout than we can.
So, this is, let's see, RPC… Common… Okay, I see, this is… Making… A common group that…
JSON RPC can extend from… do we have others? Do we have, like, gRPC? Oh, no, because we don't have a common one.
**James Thompson** 20:58 We currently don't have a common one, Right? But…
when the… once this is merged, the gRPC would also be able to use this same common and same for ConnectRPC.
**Trask Stalnaker** 21:13 Right, right. Cool.
So, if we look at…
**James Thompson** 21:24 This just needs a rebase.
**Trask Stalnaker** 21:28 Let me see… Bands… okay, so nothing effectively changed.
In RPC spans, RPC Metrics, Markdown, that's good.
So we just added with this…
Right…
So, we got… RPC method… oh yeah, let's compare…
Json RPC…
So, the old JSON RPC… Add method…
Server, okay, it did not have… okay, server address.
So… In… does your PR mention… Changes… let's see… Missions… Right, span definitions, okay… So…
adds new attributes to JSON RPC…
So, we are getting…
**James Thompson** 23:04 But does it technically add? Because there technically wasn't a definition beforehand, because it wasn't a span.
It was just a list of…
**Trask Stalnaker** 23:13 Fair, I… Yeah…
**James Thompson** 23:23 Yeah, because it's just missing accusations.
**Trask Stalnaker** 23:25 Yeah…
Yeah.
I agree with that.
No.
Okay, so server address…
Oh, I know what I want to… what we'll compare it against is then just the general…
RPC spans… So we've got system… Server address, server port… Got the JSON RPC stuff…
**James Thompson** 24:11 It might be quicker just to look at the YAML, because I'm actually extending to the base span anyway.
**Trask Stalnaker** 24:17 I… Can't. The YAML extension's confusing me too much, I have to look at the markdown, sorry.
Network peer address, network peer port.
Transport and type… RPC method and service. Okay, so we're…
Don't have… oh, we do have RPC method… Oh, yeah.
**James Thompson** 24:45 For Jason RPC, it's required. That's why it's up in a different position.
**Trask Stalnaker** 24:49 Got it. But we don't have RPC service.
**James Thompson** 24:53 Yep.
And JSON RPC doesn't have a service, so that's what I'm…
**Trask Stalnaker** 25:00 Okay.
**James Thompson** 25:04 Which is what the original issue… one of the issues that I linked talks about.
**Trask Stalnaker** 25:12 Okay, so we've got, changelog, sunspan definition…
Enhancement, RPC…
22… 2228.
Alright… Yes, these are all make sense, and we agreed on JSON RPC, no underscores… This page all looked…
Good. Client.
Yes.
JSON RPC… And then the YAML…
The YAML, I get lost in the extension, so I review the, markdown. I know it's backwards.
And then… That looks good.
Alright.
Cool. Did you want to talk about any of these draft RPC…
Oh, I see, this is just right waiting on the other one, the first one to get merged.
**James Thompson** 26:47 Yeah, like, those are done, it's just… they just need a rebase once the first one's merged in, so it gets the common.
**Trask Stalnaker** 26:55 Right.
**James Thompson** 26:56 Okay? But I did put in the agenda one to discuss.
**Trask Stalnaker** 27:05 That's fun.
**James Thompson** 27:06 Yep.
**Trask Stalnaker** 27:13 Protocol name version… a PC.
Okay…
**James Thompson** 27:23 Yeah, so I've gone through adding it to the metrics, etc.
But I don't know if we should add it to those 3 there.
**Trask Stalnaker** 27:34 Yeah, let's look, I don't even know what our… our PC metrics…
So… Okay, we've got… PC server duration…
Sure.
Okay… So, network protocol name version…
Let me see if we have…
AIM version, okay.
Conditionally required…
Not. Okay.
Okay… So… and…
**James Thompson** 28:59 It's the second tab.
**Trask Stalnaker** 29:02 Thanks.
So what would we… for RPC… Yes, we also… It would be, like…
Direct over HTTP… yes, we're fine.
Responses per RPC.
So this one makes sense to me, right? Request… Oh, yeah.
Did want to check, what do we do for… Yes, we have those there.
So, that makes sense, and so your question is those four.
Request for RPC.
And so this is going to be… Only relevant for streaming.
Which is stretch goal for this group.
I don't… oh, that's a good… so, okay, but today… I see.
Today, network… I see, so we do have all of these.
Today…
responses per RBC. I mean…
**James Thompson** 30:42 Yeah.
**Trask Stalnaker** 30:45 Trying to think of the use case…
I guess… I guess for… I don't really have… Any good…
**James Thompson** 31:00 Yeah, but the thing is that…
I was inclined… I was going to put it, but then I saw that the HTTP equivalent doesn't have it.
**Trask Stalnaker** 31:14 Okay, I mean, I… Active is pretty… Different, but let's look at…
So, what does Active have?
Let… let's see if I can remember why it doesn't have…
Oh, I think… okay, so one of the reasons… So, active…
can only use things that are available on Span Start.
Right, because it has to increment…
When, requests start, and decrement when the request ends.
So that was one limitation over here.
Which… I don't think… Is a problem for… these responses per RPC.
So what would you do? You'd keep a counter.
And when the RPC ends, so when your whole streaming thing ends… You would…
Because it's probably a histogram, right?
Let's see… Instagram… So you're not incrementing it.
As you are getting responses?
You have to store up the number of responses, and only when that whole streaming conversation Ends…
I don't really understand this metric, honestly, from a use case perspective.
It's kind of confusing.
Because so often, like, the streaming stuff, like, is often just, like.
Kind of just an open channel of never-ending back and forth over a stream.
It's not.
So this is kind of… That's all.
**James Thompson** 33:42 Yeah, I couldn't make much. I was trying to work out the use case for…
What it would actually be showing you, because… Yeah.
**Trask Stalnaker** 33:54 I… would…
Just do whatever's easiest in that case, which is probably the stamp the same… exact same attributes on them.
**James Thompson** 34:12 So, it's been done without it?
Alright, already? That's already done.
In the PR that's linked?
**Trask Stalnaker** 34:25 Okay, let's look.
So…
**James Thompson** 34:29 Awesome.
So, it literally just adds the attributes to the ones that require it.
Which is what HTTP did anyway.
**Trask Stalnaker** 34:43 Tricks… I thought you had… I thought your other PR was adding…
**James Thompson** 34:50 My other PR adds a common group, which provides the common across all metrics.
**Trask Stalnaker** 34:56 Yeah.
**James Thompson** 34:57 Alright? But…
Well, the question is, is network protocol name inversion across every single group, or is it across some, like in HTTP?
Right?
But… Yeah.
Yeah. For me.
I think… I'm inclined to leave it like this, if we don't see the need on those
Responses per metric?
**Trask Stalnaker** 35:25 Okay. Yeah, I think that's fine. I think I agree that not having it makes sense. I mean, I guess technically…
it… Could you have a different network?
protocol…
for different… I mean, I can only imagine that all the back and forth over a connection, would be over the same protocol.
So I guess probably that doesn't really make…
Yeah.
I mean… I… Expect we need to take a… Where I like it.
**James Thompson** 36:16 I also think, for me, is… we're probably likely to break that one, anyway.
Because… is that naming following conventions?
Responses underscore per.
**Trask Stalnaker** 36:29 I don't… I don't think so. Has anybody implemented this?
Maybe we… can we just delete it?
Oh, look at this! Python!
Let's see… I mean, but does that mean they're actually… no, that's just their SEMCOM, okay?
Just some kind, does anybody actually have instrumentation?
Symmetrix…
Mmm…
Go SamCom.
Some calls back… I guess I'd probably have to… it's not a totally precise search, but…
I kinda doubt that anybody is using it. I'm gonna open an issue.
And then he's
deprecate.
What are these requests, responses… So let's plan… Server requests…
Alright, well, we've got a placeholder on our board now.
So yeah, I guess, honestly, my preference, James, would probably be just to add them to the common, because that's going to be less…
Code, and that's where we would want them if we do end up Deprecating these anyways?
**James Thompson** 39:50 Yeah, so if I add it to the common, that means I have to wait for the other one to be reviewed, merged, then rebased, add it to the common.
Or, if it's directed on the attributes, it's ready to go now.
**Trask Stalnaker** 40:05 Yeah, I think that it would be good to get the other one in first, and you…
I… because it kind of doesn't really make the… this one doesn't really make sense on its own.
To me, at least.
Because it's adding these attributes here
But they've got no other attributes.
**James Thompson** 40:30 Huh.
**Trask Stalnaker** 40:31 At this point, right? Until we have the common.
So, I'm… I'm kind of, this PR… I… I get what you're saying, that technically they can… there's not gonna be merge conflicts.
But semantically, it seems… Weird to me.
**James Thompson** 40:50 Nope.
**Trask Stalnaker** 40:56 Alright, steve, I'm guessing this was you.
**Steve Rao** 41:02 Yeah, yeah, maybe that is, related to the implementation, yeah.
**Trask Stalnaker** 41:07 Yeah… Alright, let's see what, RPC metrics you're capturing. Okay, RPC server duration…
Oh, that's a test, okay, yes.
**Steve Rao** 41:21 Yeah.
**Trask Stalnaker** 41:23 Chain test, okay.
our PC server metrics… Oh!
So that was really easy.
**Steve Rao** 41:34 Yeah, yeah.
**Trask Stalnaker** 41:34 I mean, other than tests.
**Steve Rao** 41:36 But it's a discussion, yeah. Do you have any comments?
**Trask Stalnaker** 41:43 Let's see, let me just take a look. So, basically, it works because… It implements…
Now, let's see our RPC metrics…
**James Thompson** 42:03 Do we hold off on this? Because we want to change the unit…
**Steve Rao** 42:12 Yeah.
**James Thompson** 42:13 Alright, we want to change from…
We want to standardize it to seconds.
Alright? We'll have the breaking change of…
The system name field being changed, as well.
Right? Should we hold off until those specs are done? That way.
This implementation can directly follow the new spec.
**Trask Stalnaker** 42:36 So what we'll probably do, the same that we've done in the Java instrumentation for HTTP and database, is they all sort of share this common infrastructure.
And so, we just update the common stuff.
And that propagates out to all the… instrumentations.
And we'd do the whole opt-in flag, deal.
But it's true, I mean, it does expose by landing it Now, it exposes…
Users to a breakage.
Yep. That they wouldn't have.
Otherwise.
I know that… I know that this one came from a user request.
Though, so…
**Steve Rao** 43:36 Yeah.
**Trask Stalnaker** 43:43 I guess, I'll leave that, Steve, since you, are sort of maintaining the double instrumentation.
**Steve Rao** 43:52 Yeah.
**Trask Stalnaker** 43:53 I, I'm comfortable, I'm comfortable.
Either way, going either way on this one.
It could be… a few months before… we're still trying to get the database
instrumentation stabilized, so it could be a few months before we get to RPC instrumentation in the Java repo.
**Steve Rao** 44:15 Okay.
**Trask Stalnaker** 44:24 That's all work.
So… Verifying…
Were you… did you try using satisfying exactly?
I forget if we're able to do that.
To confirm that there weren't any additional attributes that aren't… Verified.
I'll leave a comment, you can… Take a look.
**Steve Rao** 45:00 Okay.
**Trask Stalnaker** 45:18 And I forget if we are doing that in other places, too.
**Steve Rao** 45:24 Okay.
**James Thompson** 45:26 Should we leave out network.type, considering that will be removed?
And it's not currently a required field.
**Trask Stalnaker** 45:38 I'm guessing, right, this is all flowing from writing this one line of code?
**James Thompson** 45:45 Yep.
**Trask Stalnaker** 45:46 So, I would… Prefer not to start
going into the RPC, the core pieces of the Java RPC, instrumentation.
I'm just… Test what we're getting at this point from this one line of code.
Alright, cool, we've hit our 45-minute window.
Thank you very much.
And Steve, I will see you in 15 minutes!
Alright, take care.
**James Thompson** 46:30 Bye.
