SIG: RPC Sem Conv Stability SIG
Date: 2026-06-11
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 05:15 Hey, folks!
**Matthew Hensley / Grafana Labs** 05:20 Hello.
**Steve Rao** 05:21 You trust?
**Trask Stalnaker** 05:25 Hey, mad.
**Liudmila Molkova** 05:27 Hi, folks!
**Trask Stalnaker** 05:49 Alright, so, why don't… I think, Marav, I think, primarily, we want to discuss… Your findings, your… Issues, concerns…
**Madhav Bissa** 06:07 Alright, Trask. So, essentially, I am still going through… there is a lot of scattered documentation, like, we have one documentation for… Specifically, gRPC semantic conventions, and then we have some things just separately for RPC spans, separately for RPC metrics, and… We also have that compatibility document, so I am… taking, that the gRPC semantic conventions and the compatibility document takes precedence over the generic RPC span and RPC metric.
Documentation that we have.
**Liudmila Molkova** 06:49 Yep.
**Madhav Bissa** 06:51 Okay.
**Trask Stalnaker** 06:51 the compatibility… Doc is… is non-normative.
I mean… Isn't it?
Moving a lot?
**Liudmila Molkova** 07:05 Oh, I thought might have, you mean that, the gRPC doc takes precedence over RPC doc.
**Madhav Bissa** 07:14 Yeah.
**Liudmila Molkova** 07:14 So maybe… bear with me, let me share, and we will… so we are talking about the same thing.
Give me a sec… Friend… Okay, so this doc… Takes precedence over… This one.
And other things here.
**Madhav Bissa** 08:00 Okay.
**Liudmila Molkova** 08:01 And… This friend… oh.
Didn't we have… the compatibility. This one is non-normative. It's just the… for information.
**Madhav Bissa** 08:16 Okay.
Fair enough. So, I'm still working through, each, field. I was reading through, documentation in other places as well, but, the, like, there are a couple of things that… people have flagged to me in the RPC team, which I'll erase and get the conversation going. I will send across The findings or a document separately in writing so that we can all collaborate on it.
Maybe in the Slack channel or something later on.
But I wanted to start the conversation going, around the gaps. So, first issue that I think the gRPC team actually had is around the status code, because we mark it as the RPC response status code, and semantically, gRPC doesn't… mark the status, and it's not necessarily a response status code, it is generally just a status that can come from the client or the server. It could be response or without the response itself. So… But I see it smart as… Release candidate already, so… I don't know what can we do around over there.
**Liudmila Molkova** 09:39 We can. The release candidate is not stable. We can still change things, but… I… Sorry, I missed the first point. I'll reply to the second, and let's… let's get back to the first one. For the response data scot, we had… I remember we had a lot of discussions around this.
And, essentially, the… It's interesting what means a response.
And in the… we realized that since we think about it as something, more, like, logical.
And, like, a physical request and response.
The response is the response to the user from the API.
Users might not care who generated this thing, client or server.
And also, in all other conventions, not RPC, we have Response status quoad.
And it made sense to align across different conventions.
I don't know if… does discussion as… like, how important is discussion to you on a scale from 0 to 10? Like, would it be a blocker for a gRPC team to… Switch to… RP series.
**Madhav Bissa** 11:00 odds.
**Liudmila Molkova** 11:00 Obviously, this card, or…
**Madhav Bissa** 11:03 So, it is, semantically, the moment I pitched it to the team, they were like, but this is wrong, and it denotes what we don't really do in gRPC, so it will basically change the meaning of the status that we are publishing currently, and If we just mark it as RPC status code as well, How does the semantic meaning become any less rich, is what I am trying to understand. So, whether it's a blocker or not is a separate, Question, I'm just trying to first identify the gaps and, like, Do we have… Like, if we make it more generic, we will… Pull… we will separate it from the discrepancy that it adds to the semantic meaning that… I'm… That is what I'm trying to gauge.
**Liudmila Molkova** 12:06 It's… it's more of a, like, a consistency with other conventions that we have.
I… Personally, I don't feel super strong about it.
**Madhav Bissa** 12:18 Oh, okay.
**Liudmila Molkova** 12:18 I can't live for us either.
I'm curious if someone on this call feels strong.
**Trask Stalnaker** 12:27 Yeah, I'm checking from a consistency perspective, So… I mean, HTTP response status code is an actual… Response status code, because it maps to the protocol.
Db response status code… Trying to think what that…
**Liudmila Molkova** 12:59 Oh, I think it's a mix. Sometimes it comes from a client, sometimes it comes from the server.
And maybe we thought that if we did it for DB and HTTP, well, for DB, there's this caveat, that we also do it for our PC. That's what my memory tells.
**Trask Stalnaker** 13:19 Yeah.
Yeah, I mean, potentially that's what was missing, Madhav, for people to understand why its response status code is that this whole modeling is at the logical layer.
As opposed to, we're not modeling the physical, the protocol layer.
Right, because it is the… to a… Client to a user, who caused GRPC.
It is the… they are getting back something. It's the result.
It's the response, it's the logic.
**Madhav Bissa** 14:16 Yeah, it is the choice of, choice of word, like, when you say result and when you say response, they, they, there is a slight semantic difference in there, like, And when you say result, I feel more aligned with it, but when you say response, because of the way we term things, like, in any RPC, you'll have a request and response. It… it… Kind of goes to imply that this is coming from the response, right?
**Trask Stalnaker** 14:48 Yeah, that's fair. Okay, so I think we understand that concern. Let's, let's… continue, and I think it would be in the… in this… in our 30 minutes here, it would be helpful to understand the breadth of all of the concerns.
**Madhav Bissa** 15:04 Yes, and one of the other concerns, that, I was finding was around the server address and port. So, currently, there are… gRPC has a lot of different schemes in which the target is specified. It's not necessarily always complying to server and port.
format. And I think, in the compatibility document or somewhere, it is mentioned that Where not possible, you can just use the target as is in the server address field, and leave the port blank.
So… But the description, for those, fields.
Explicitly mentions that we should have a server address and a server port.
**Liudmila Molkova** 15:58 Can you… showware?
**Madhav Bissa** 16:04 Yes, I'm just lost between the documents now. Just a second, let me… Figure it out.
So, for instance, you have PC, yeah.
address… Yeah, so the description for server address in the gRPC semantic conventions, it says… may contain a DNS name, an endpoint, And part-in service registry.
local socket name, or an IP address?
And…
**Liudmila Molkova** 17:12 Okay, I… I am sharing, so this is the gRPC doc, this is the server address, group of architects.
**Madhav Bissa** 17:19 Yeah, you have detailed description, below the table.
**Liudmila Molkova** 17:35 So, up where…
**Madhav Bissa** 17:40 Alright, just…
**Trask Stalnaker** 17:43 Search for may contain.
**Madhav Bissa** 17:51 Yeah.
**Liudmila Molkova** 17:56 Oh, and this is the… Server. Why do we have server address on the servers, Ben?
**Madhav Bissa** 18:04 Yeah.
**Liudmila Molkova** 18:08 Should I remove server addresses from the servers file altogether?
I mean, let me just create an issue. I think, yeah, this is not proof.
I don't know what we should put for the server address on the server span, maybe just remove it, but yeah, you're right.
We can easily change this to be something more accurate.
**Trask Stalnaker** 18:44 Cool. Was that the only concern about that, Madoc?
**Madhav Bissa** 18:48 Yes, and .
**Trask Stalnaker** 19:03 I'm taking notes also, Lydnilla.
**Liudmila Molkova** 19:07 Yeah, thanks, I'm logged in as wrong user. Yeah, thanks.
**Madhav Bissa** 19:15 Yep, those, that was the… Yeah, that's the only, that's the only con… yeah, only concern about server address, like, why on the server side do we have server address?
And.
**Liudmila Molkova** 19:42 You mentioned before we started talking about, the… Status code. You mentioned some other concern, and I missed it. Was it the server address one?
**Madhav Bissa** 19:55 No, in the status code, we spoke about the response, not…
**Liudmila Molkova** 20:01 Before that, you mentioned something, and I missed it.
Something…
**Trask Stalnaker** 20:07 I think we've only heard two concerns so far, the status.
**Madhav Bissa** 20:10 Yeah, and the server address.
**Liudmila Molkova** 20:12 Oh, awesome. Yeah, sorry.
**Madhav Bissa** 20:14 There's only those two things, yes.
Oh, that's it?
**Trask Stalnaker** 20:17 Nothing… nothing else?
**Madhav Bissa** 20:21 No, no, I'm saying we've discussed only two so far. Oh, okay, great, yeah.
**Trask Stalnaker** 20:25 Yeah, let's move on. Yeah, thank you.
**Madhav Bissa** 20:28 So, I did make a list of all the concerns, but… I am still… Doing a recon, around… how valid those concerns are before I bring them to you, which is why I have not yet published them, because I just wanted to be sure I'm reading the right documentation and raising the concern.
And I was just getting lost in a lot of places.
**Trask Stalnaker** 20:56 Okay.
**Madhav Bissa** 20:57 Yeah.
So, one thing that I was confused about was the error type. Since we have the… status, What does the error type actually denote? I was confused around that.
**Liudmila Molkova** 21:20 Yeah, so, think about metrics.
Somebody needs to know that for this specific metric name.
The information about status is captured in that specific attribute.
it… Sometimes it's problematic to know, because, like, complication gets… A few dozens of this… of metrics like this for different operation durations.
So… Also, the error, the status card is not any indication of an error.
Right? So, even… Like, okay is okay, but the rest is blurry.
So, from the application perspective, if I'm Saying, that application.
Oh, sorry, the request was canceled. It can mean a lot of different things, right?
our deadline exceeded, or anything. It can mean a lot of different things, and usually.
What we do is that we have the serotype attribute first, it appears on pretty much every metric and span.
And it tells the… the presence of it tells if… To the best of our knowledge, this operation was successful or not.
And… Also… it captures… like, for gRPC, it's probably less important, but for, many other protocols, the status quoad Sometimes happens… Sorry, exception happens without status code.
And you need a place to capture all of those things. And, for example, I would… I don't know what your PC clients do, but I would imagine that at least some RPC systems, when Exception happens, during the validation phase, before anything has started. They will throw an exception.
And would not return any response code at all.
**Madhav Bissa** 23:31 Okay.
Understood.
Okay, that makes sense.
I'll just run it through a bunch of scenarios that I can think of, and then see if there is any issue with that or not.
But sounds reasonable to me.
And, So, other thing was, the network peer address and the network peer port that we are talking about, like, how do we want it to be different from server address and server port?
**Liudmila Molkova** 24:08 Yeah, so for… this one would be, let's say, an example.com.
Right, or whatever.
**Madhav Bissa** 24:15 Yeah.
**Liudmila Molkova** 24:16 I think this is IP address behind it, if we know it.
**Madhav Bissa** 24:22 Okay, right. And if we don't have IP, Then, what do we fall back to?
Or we just leave it blank.
**Liudmila Molkova** 24:31 Nothing, we're just unpopulated. Yeah, leave it blank.
**Madhav Bissa** 24:35 Okay.
And, other interesting thing that I saw was RPC request metadata.
This is, essentially, are we allowing users to configure, custom fields that are going on Going in along with… The request.
**Liudmila Molkova** 25:04 Yeah… Sorry, I think I've lost the purpose here.
So, you don't have to implement this feature in your instrumentation, but you may, allow users to say, okay, Enable the specific metadata properties, and then for each property, they enabled You would populate the attribute, with that name.
We can share some examples, maybe, of how it's done.
The.
**Madhav Bissa** 25:41 Yeah.
**Liudmila Molkova** 25:42 options.
**Madhav Bissa** 25:43 Like, because it talks about the key, and, like, is it like a… So we're basically expecting a key-value pair, right?
There.
**Liudmila Molkova** 25:55 A list of keys to… yeah.
**Madhav Bissa** 26:00 Okay, because we also have something similar in gRPC, I was just wondering if we can map it to this. We do allow custom labels, but… slightly different semantically, I'll just have a look if we can… Find some resemblance there, or if there are use cases, then we can enhance this specific feature.
**Trask Stalnaker** 26:22 So this is specifically for the metadata… part of… It's not… Any custom label?
Yeah, I think Linda's pulling up, So, like, the configuration would be users could say, I want these specific metadata fields captured in my on my span.
**Madhav Bissa** 26:51 Alright, but, the explanation below, it says my custom key, is that just for example, or… If you'll go to the description below.
You can search for instrument, number 8, I think, yeah.
So, if you'll see the… example, given that part, it talks about my custom key with value, attribute value should be recorded. So, I was just confused, is this custom key something that the applications are defining, users are defining, or is it.
**Trask Stalnaker** 27:26 Users, yeah, so that would be the, the explicit configuration of which metadata values to be captured.
So the user would say, capture, I want to capture my custom key.
**Madhav Bissa** 27:45 Anyway…
**Trask Stalnaker** 27:46 configure that.
And then the instrumentation would capture my custom key whenever it appears in the metadata.
**Madhav Bissa** 27:57 Okay.
**Trask Stalnaker** 28:01 We do something similar… we do the same thing on HTTP.
Where, users can pick which HTTP headers, if any, that they want to capture on the spans.
**Madhav Bissa** 28:18 Okay.
Okay, cool.
Fair enough. If you can, so I'm still… thinking, so… metadata… by itself contains, let's say, X number of headers and values, right? Keys and values, right? Now, by defining this, if… The protocol itself allows users to also add information in the metadata.
Then, by using this, users will be able to Capture that information also as a part of the metric.
**Trask Stalnaker** 29:02 Right, it's… it's an allow list of explicit keys, just because we don't, have… want to capture everything from a…
**Madhav Bissa** 29:12 Yeah, that I understood, but I'm trying to understand the intent. Is there… are there some specific, metadata, keys that we know of, which usually, like.
what basically was the inspiration to add, this is what I'm trying to understand, so that I can understand the use case better.
Is there some specific metadata key that… You have seen, as a practical usage in some other protocol, or…
**Liudmila Molkova** 29:46 like, let's say for HTTP, I was just, more… much more familiar with HTTP than gRPC.
imagine people want to capture, some custom correlation keep, I don't know.
X correlation AD, or some kind of… this. And it's specific to the application, what's in this header.
And if they pass things over gRPC metadata, oye… there is something there important for their application. This is the extensibility kind, and they would configure it. It's not about specific… like, the use cases, users want to extend the information, they…
**Madhav Bissa** 30:43 Okay, fair enough. So, what I wanted to understand is, let's say if it is HTTP, and if there is something like bearer token that is being passed in the header, can the user just configure that, and then that starts getting emitted? Isn't that, like, a security risk?
**Liudmila Molkova** 30:59 They opted in into this by explicitly enabling that specific key, that's the mitigation.
**Trask Stalnaker** 31:04 Yeah, that's why we don't allow star…
**Madhav Bissa** 31:09 Okay.
Okay.
Fair enough.
**Trask Stalnaker** 31:14 And I would say, I don't know, how many… of the existing gRPC instrumentation support this, even? I know the Java one does.
It, you know, it would be fair if the GRPC team doesn't want to support this.
Opt-in thing initially, and wait for a user, you know, user… specific user requests, if you want to understand the… that those use cases better. This is not a… I don't see this as a critical piece of, you know, 1.0.
**Madhav Bissa** 31:54 Alright, fair enough.
Cool. So that brings me to the last question before we close off, is do you have An absolute must-have list of things that you need for 1.0 OTL stable release for gRPC semantic conventions.
**Trask Stalnaker** 32:16 I mean, I would go… just assume that it's everything that we've marked as RC.
**Madhav Bissa** 32:22 Okay.
**Trask Stalnaker** 32:22 provide feedback otherwise.
**Madhav Bissa** 32:26 Okay.
**Liudmila Molkova** 32:29 Or, if you see something in the description of the stable thing, so this is, tailored to… RPC.
To gRPC, right? So we can update most of those things, like, we cannot change the meaning of the server address, but we can narrow it down to something, so all of… most of the things you see here are opt for… .
**Trask Stalnaker** 32:58 refinement.
**Liudmila Molkova** 32:58 Clarifications, yeah, for climate.
**Madhav Bissa** 33:01 Okay.
**Trask Stalnaker** 33:02 That's good. I saw you, Lyudmila, you were, that request metadata key is actually not part of RC.
If you see it, it's still in development, so…
**Madhav Bissa** 33:13 Yep.
Okay, and so the server address is marked as stable for the server side as well, right? So you would be removing that anyhow still, right?
**Trask Stalnaker** 33:27 So this whole document, if you look at the top, the whole document is release candidate.
It's a little confusing.
The stability marker there is because the attribute itself has been marked stable elsewhere as a general attribute.
Okay. But we can…
**Madhav Bissa** 33:48 Okay.
**Trask Stalnaker** 33:49 include or exclude it from here, this document, we can refine the…
**Madhav Bissa** 33:54 And they're like.
**Trask Stalnaker** 33:54 language.
**Madhav Bissa** 33:55 So the spec itself can change, cannot change because it is stable, but it could be excluded or included in the… In December. Okay, understood.
**Trask Stalnaker** 34:05 We can… we can do more than just include, exclude, as Lyudmila mentioned, we… we can change the text here, so we… in GRP… in each convention, we can override and kind of clarify what it means in that specific convention.
What we can't do is change the name of server.address.
**Madhav Bissa** 34:27 Understood, yeah, that's what… understood.
**Liudmila Molkova** 34:29 Yeah.
**Madhav Bissa** 34:30 Okay.
**Liudmila Molkova** 34:30 You don't… You need to… you don't have to think for us about what we can or cannot do, you can just bring concerns, and we will talk through them and decide, like, most of the time, we probably can address them at this stage.
**Madhav Bissa** 34:45 Alright, so that… that's a big relief. Thanks.
Cool. So I am pretty much through with documenting all of this. I'll just get, review done from my leads, and once they have some more things to add, or, you know, if they have any comments.
I, I will send across the detailed, findings in Slack, probably, or straight up, or over email, whatever you guys prefer.
I joined.
**Trask Stalnaker** 35:13 An issue, if you're… if you're comfortable opening an issue, that would.
**Madhav Bissa** 35:18 I can look at GitHub issue as well. Yeah, yeah. Okay, sounds good.
Alright. Awesome. I think.
**Liudmila Molkova** 35:23 Thank you.
**Madhav Bissa** 35:24 That's all for today. Thank you. Cool.
**Liudmila Molkova** 35:25 Thanks, bye-bye. Bye. Thanks, bye.
