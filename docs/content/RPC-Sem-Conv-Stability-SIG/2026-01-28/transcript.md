SIG: RPC Sem Conv Stability SIG
Date: 2026-01-28
Duration: 52 minutes
============================================================

## Zoom Recording Transcript

**Steve Rao** 02:18 Hello.
**Trask Stalnaker** 02:21 Steve?
**Steve Rao** 02:22 Yeah, hi, Chaska.
Yeah, Ludumino said he will join us later. Let us wait for a minute.
**Trask Stalnaker** 04:12 Oh, okay. Thanks.
**Liudmila Molkova** 06:12 Hello!
**Steve Rao** 06:15 Hello.
**Trask Stalnaker** 06:15 Hey.
**Liudmila Molkova** 06:18 Okay, Andrew Knot Staker is back. We did miss you.
**Trask Stalnaker** 06:24 No, this one you can't, opt out of, either.
When I first joined, I was outnumbered 2 to 1, but the, one of the… I like the bot that allows you to opt out.
**Liudmila Molkova** 06:38 Yep.
Okay, so let's see… We are… In the RPC world… So I wanted to… Talk about network protocols, we started last time.
I think we should also take a look at the double.
conventions?
Thanks, Steve, for updating them.
And I also wanted to… Bring back the… GRPC target.
I merged, oh, I'm blanking.
I merged the immigration guide.
**Trask Stalnaker** 07:55 Oh, okay.
**Liudmila Molkova** 07:57 So… Okay, and I created… This difference. They are on the agenda.
We'll move them somewhere… And… This is also on the agenda. This is on the agenda.
this is… It depends on the… target discussion. So I think we don't need to do anything on the board.
Okay, so, we started this conversation last time about the network protocols.
And we wanted to entertain the idea of Maybe removing them?
The protocol name version.
Transferred, maybe?
So… I… have a PR to… just to remove them.
So… When it comes to… RPC, right? We consider it logical.
**Trask Stalnaker** 09:30 Yeah, I feel like that's kind of where… I'm coming down on removing, like, why I like removing them, is I feel like it aligns more with database.
Which were… It's logical.
And we've kind of modeled… I mean, and I think that's kind of some of the original confusion, and I think that goes to James's… PR about protocol versus framework.
And… We've basically… we're saying… RPC semantic conventions models today models the logical layer.
So… That's kind of the answer to the… as opposed to the protocol.
Layer.
**Liudmila Molkova** 10:19 Right.
We also wanted to check if this information is even available.
to the instrumentation.
And it's not, at least not really, really, for gRPC and connector PC.
And we talked that it might still be interesting to, let's say, if you're using ConnectRPC and you support multiple protocols.
to record what… Somebody used when they called you.
And this is actually content type.
And it's available through headers.
So, I think the important part of this discussion, let's say.
Somebody wants to use it on metrics.
Should we make the request metadata opt-in on metrics?
Separately from Spence?
There's two different ways to configure it.
**Trask Stalnaker** 11:30 Sorry, can you say that again?
**Liudmila Molkova** 11:34 Imagine…
**Trask Stalnaker** 11:35 different ways of…
**Liudmila Molkova** 11:36 let's say we make RPC request metadata opt-in, On spans and metrics.
And then… What you capture on spans in metadata is not the same what you capture in metrics.
as metadata.
It would be two different sets of… Attributes.
**Trask Stalnaker** 12:08 If we kept the network attributes, then follow.
**Liudmila Molkova** 12:13 I think this is orthogonal, right? This is, like.
**Trask Stalnaker** 12:16 You would want them to be different because of potential cardinality?
Issues on metrics? Yeah, yeah.
**Liudmila Molkova** 12:22 Yeah.
So maybe it's a good idea to separate… separate this issue, break it down in two, because this is, like… or if we don't capture The network protocol name and version.
Is there something that's still missing?
And… there might be.
Like, this part, the content type.
**Trask Stalnaker** 12:55 And if there really is a network protocol in play, I mean, you can… Still use that attribute.
like, I'm thinking for database, even though, like, it's logical spans, like.
If you wanted to enrich it with something more, like, if you knew, like, Cosmos.
You have the logical span, but if you know which… which protocol it's talking… Good.
Still use that, if it fits.
**Liudmila Molkova** 13:45 Yeah, so, like, I think Steve is proposing to add network protocol name version to double.
And it should be fine for individual conventions to reference it if it's necessary.
**Steve Rao** 14:03 Yeah, okay. Yeah, at first, I just, referred other… other semantic convention, like gRPC, to add that port.
And, yeah, for me, currently, in RBC semantic convention, or in, Java instrumentation, implementation, we don't support that.
So, if we remove it, I… I can't come up with an inset effect currently.
**Liudmila Molkova** 14:40 Mmm. But you would still want to capture the… The fact that it's double 2 versus double 3 in some way, right?
**Steve Rao** 14:49 Yeah.
in… in… in current PR, yeah, I steer, a comment.
Comment that.
But I… we discussed, yeah, last week, we want to move that.
In other RBCs, so, I don't, remove it, immediately.
But… but I found you, create a PR, I want you to move them from, the RPC's main convention.
Yeah, if, it's reasonable, I think, yeah, maybe we can remove it in double.
for me, currently, I don't come up with other side effects if we move it there.
records in current Java instrumentation implementation.
We don't… a capture.
a related attributes.
**Liudmila Molkova** 15:50 I see.
So… Can we… Indefinitely postpone distinguishing 002 from 003.
**Steve Rao** 16:03 Hmm.
Hmm, yeah, I think it's okay.
for… Normally each, customers, maybe they, yeah, they… they can observe it according to the, version they used, framework version they used.
If they use double 3, Usually they use the triple protocol.
By default, if they use the double, 2.0, they use the W2 protocol by default.
**Liudmila Molkova** 16:43 That's on the client and on the server.
**Steve Rao** 16:48 Yeah.
**Liudmila Molkova** 16:51 And on the server, oh, you wouldn't have any indication on the server.
of… So on the server, somebody can connect to use 32 and through triple.
**Steve Rao** 17:07 Yeah, maybe in, in double 3, they can use triple, but in double 2, 220, they can't use triple protocol.
It doesn't support.
that protocol. It's introduced in 3.0.
**Liudmila Molkova** 17:29 But, like, on the server, on the serial server.
the Serio server can support both?
**Steve Rao** 17:38 Yeah.
Sorry, maybe, I, I think, yeah, maybe in 3.0. I'm not sure, maybe it can't support 2.
Yeah, maybe just supports a, payPal protocol.
That is also default, protocol.
And other option, like the documentation introduced, it's a HTTP protocol in W3, but it's rarely used.
It means I don't have many users to use that.
Maybe triple, maybe we can just come up with, to think about in triple.
I think, yeah, for the first step, maybe it's enough.
**Liudmila Molkova** 18:52 The key question… okay, let's say we remove it everywhere.
It's… Not to make things worse, but… We won't be able to add metric attributes.
In the future.
**Trask Stalnaker** 19:15 By default. By default, yeah. It could be… Dan.
**Liudmila Molkova** 19:22 Right.
**Trask Stalnaker** 19:24 And… kind of feels like something… I mean, I don't… I think it's a reasonable opt-in, because it's sort of like, well, if you… Limited use users who want to differentiate.
Bad.
Most people know that, for example, in Dubbo, they know they're using Dubbo3 everywhere.
Or they're using 002 everywhere, like, it's not probably that interesting of a question.
For most people.
**Steve Rao** 20:01 Yeah.
**Trask Stalnaker** 20:03 And so, opting in… Seems.
Maybe even better, because it… You don't. Saves… saves a telemetry cost.
For the majority of people.
**Steve Rao** 20:19 Yeah, I have a small question. Yeah, here, opt-in means, if any users want these attributes, maybe we can add them later.
**Trask Stalnaker** 20:30 Right.
What we can't do, Steve, in, in metrics, Adding new attributes into metrics.
Is often considered breaking.
**Steve Rao** 20:46 Hmm.
**Trask Stalnaker** 20:47 Or some… complicated reasons.
But we can… Add new attributes to metrics as opt-in.
**Steve Rao** 20:59 Okay.
**Liudmila Molkova** 21:00 So that users would enable them explicitly.
So, Rusam option.
**Steve Rao** 21:10 Okay.
**Liudmila Molkova** 21:13 Cool. So Dan, it sounds like we can just remove them.
And then… Also in this PR.
And… This… oh, you already approved, Trust. Very fast.
**Trask Stalnaker** 21:36 Well, right, like… 5 seconds ago, I was waiting for our conversation to end. I was gonna click approve at the beginning of our conversation, because I knew which direction I was leaning, but… I figured I should wait.
**Liudmila Molkova** 21:54 Okay.
So then, let's move on to the double conventions. Oh, that's… that's just… Leave a small comment… That this becomes easier.
**Steve Rao** 22:14 Yeah.
**Liudmila Molkova** 22:31 And then, Steve, do you think we need to talk about something here? I only had some minor… comments, I believe.
**Steve Rao** 22:40 Okay.
Yeah, for this point, I think it's okay, yeah. The, the… The comments on screen.
**Liudmila Molkova** 22:52 Quay.
And then this comment disappears.
This comment also disappears with this.
Okay, and then there's just one comment from my site on the… The number versus string.
**Steve Rao** 23:16 Okay.
**Liudmila Molkova** 23:40 Okay, so then, moving on to the GRPC target, so… Last time we talked, I'm going to… Okay, anyway closed?
Oh, I know.
We are very aggressive with closing PRs.
Okay, so… Last time we talked about gRPC?
And… that when someone configures gRPC, they provide a target string, which could be a valid URL, or it could be… Just a string.
your PC knows how to interpret it.
**Trask Stalnaker** 24:50 Right?
**Liudmila Molkova** 24:52 We are going to parse server address server port from it, because it's super common.
And in the past… in the past iteration, we considered using URL scheme to record this part.
And then it still left some of the… Possibility. Some of the formats, were not possible to record.
So what I'm suggesting is, and we started talking about that last time, is to… just capture the gRPC target, as Inktrascu suggested, instead of scheme.
So… Should have some examples… Here… Here I go.
So… The suggestion is to capture it if it contains any information that's not available in server address and server port.
So for this case, it won't be set.
And, like, the way you can differentiate is, let's say in Java or .NET and some other languages, there are two APIs. You either create from address, or you create from target string.
**Trask Stalnaker** 26:13 And…
**Liudmila Molkova** 26:15 This way, you don't have to… Make conclusions, and you can just provide address and port in one case, and probably all three.
In that other case.
**Trask Stalnaker** 26:33 Yeah, let me… I'm looking for your language. Let's see, if the channel was created with a target, and it contains information… Not otherwise captured in server and port.
That's saying something slightly different, I feel, than what you just said.
So if it was created with a target.
If it's a simple target, that's just server… Or… Or is that even a sim… or no, does Target always have to have a scheme like HTTP or HTTPS?
**Liudmila Molkova** 27:12 No, it doesn't. It doesn't. They would normalize it.
to DNS.
So somebody can provide this target string.
**Trask Stalnaker** 27:23 Okay.
If they do that, is that correct, with the two colons?
**Liudmila Molkova** 27:31 Oh, no, thanks.
**Trask Stalnaker** 27:33 Okay.
So if they do provide that, as the target.
Would… are you proposing to… Only capture server address and server port, or all three?
**Liudmila Molkova** 27:51 I actually prefer not to capture it if it's already in the address and port.
And maybe instrumentation can be a little bit smarter than just relying on the API.
**Trask Stalnaker** 28:04 Okay.
**Liudmila Molkova** 28:09 Okay, so Dan, for cases like this, which are… Rarely supported, and hopefully rarely used. We would capture it.
Only as the target.
**Trask Stalnaker** 28:26 Right. Wow.
**Liudmila Molkova** 28:28 And… And this creates an interesting situation on the metrics.
So… We wanted to be on… Okay, so do… do we… is it important enough, this additional information?
to be captured on GRPC metrics.
And the only case where I think it is… is… When there is no server address and port.
And then… I would like to document it here.
But that's the way to document. This is the markdown only. This is the metric refinement. We are not changing the definition, but we are customizing it slightly for the gRPC case.
**Trask Stalnaker** 29:55 Okay.
So you have this already here.
**Liudmila Molkova** 30:01 Yeah, and I'll polish it, I was in hurry when I wrote it down, but yeah.
So, with this, I think the important question… is to figure out if it's applicable beyond gRPC, and if there is a need to do anything else.
I remember we chatted about it with you, Steve?
I wish to comment, preferred…
**Steve Rao** 30:38 Yep.
I'm not very clear about, that, third con- case.
To duplicate her?
Yeah, maybe, Ying… Yeah, in normal IPC communication.
Yeah, maybe this address is not the server address.
I guess the DC's, Registration center, donate.
Nin.
Yeah, so, so this case, just want you, to, show in… Yeah, in, yeah, maybe client or server communicate with, registration center.
**Liudmila Molkova** 31:31 Yeah, so the client under the hood will communicate with a zookeeper or anything else.
But that is, like, the internal logic.
Weird.
**Steve Rao** 31:43 Okay.
**Liudmila Molkova** 31:44 Wouldn't see the fact of the communication, but it could be the only thing that we know about the Endpoint we're talking to.
**Steve Rao** 31:53 Okay, yeah, makes sense, so… Yeah, to see the migration.
Yeah, I think, yeah, maybe for, yeah, double, maybe we can also add a related remind.
But, usually, in double implementation, especially in Java instrumentation, the address… the server address, the server port we get.
by, load balance. So usually, we just have a single, destination, donate or address.
**Liudmila Molkova** 32:29 See?
**Trask Stalnaker** 32:36 It's a server-side load balancing, not as opposed to client-side load balancing.
**Steve Rao** 32:46 In inclined, inclined site is also used the load balance to select, a final address.
**Liudmila Molkova** 33:15 Yeah, I think I found the suitkeeper example somewhere in the… yeah, here we go.
**Steve Rao** 33:20 Yeah, maybe you can… Yeah, here.
**Liudmila Molkova** 33:29 So, what's registry?
**Steve Rao** 33:34 Yeah, this is, registration center address.
I just like a zoom keeper, or Narcos.
Yeah, Nakos is also… registration, framework.
It can be used in double.
**Liudmila Molkova** 33:55 Is this the client config, or the server config?
**Steve Rao** 33:59 Yeah, maybe both.
**Liudmila Molkova** 34:02 Yeah.
**Steve Rao** 34:03 For server, they will register their address, instance.
And, for client, they will use this address to get the server instance.
**Liudmila Molkova** 34:21 And what would I con… like, let's say I have some set of registries.
this is what I would give to the client, or how would I, configure my client?
**Steve Rao** 34:37 Yeah, maybe just, just one configuration. It can be used in client and servo.
**Liudmila Molkova** 34:44 Yeah, but I mean, what would I write?
**Trask Stalnaker** 34:46 followed.
Yeah, do you have the, maybe the Java doc, or the example of the method that you would call?
**Steve Rao** 34:59 Yeah, maybe you can search the Apache double related example in GitHub. Yeah, there is a project to show some Yeah.
Yeah, in GitHub.
Also, awesome Java, yeah, maybe something like that.
No, here, you can search on the…
**Liudmila Molkova** 35:28 samples?
**Steve Rao** 35:31 Let me check… Oh, okay, I shall a link.
**Trask Stalnaker** 36:10 This is what, copilot told me.
**Steve Rao** 36:15 In chat, in chat.
**Liudmila Molkova** 36:19 I don't see anything in the chat.
**Trask Stalnaker** 36:21 Sorry, I put it… I was still talking to one of the… Bots, the notetaker bot.
**Steve Rao** 36:26 Sure.
In our meeting chat.
**Liudmila Molkova** 36:35 Maybe you're also talking to the bot? Because I… I don't see… this is… this is what I see in the chat.
**Steve Rao** 36:41 Okay, okay, yeah, I'm sorry, I sent it to the bot.
**Trask Stalnaker** 36:47 Yeah. Oh, yes. Damn it.
**Steve Rao** 36:53 Okay.
**Liudmila Molkova** 36:54 And which one…
**Steve Rao** 36:56 The advance, yeah, you can check Advance.
There are some… Yes, cold tongue.
Yeah, service, discovery, yeah, maybe.
No, let me check.
**Liudmila Molkova** 37:34 Consumer, I guess?
Maybe… API?
It's too much magic for… for me.
**Steve Rao** 37:58 Boom.
Yeah, sorry, maybe GC is not, Yeah, good project to show the example. Let me check.
Yeah, wait a moment, yeah, let me check.
Mmm, okay, yeah, I sent her a new… Knew you.
Have a link to the… our channel.
**Trask Stalnaker** 39:01 I didn't… oh, yeah, cut it.
**Steve Rao** 39:05 Yeah, you can see this is, yeah, this is the demo. Yeah, you can, yeah, this is the, registration address.
Knuckles, it looks like a zookeeper, and you can see… this is a provider. You can… Yeah.
Go to the consumer.
**Liudmila Molkova** 39:25 Oh, okay.
**Steve Rao** 39:26 Yeah.
**Trask Stalnaker** 39:29 So it's vanilla, it seems.
**Steve Rao** 39:31 Richard.
Resource. Yeah. Sorry, resource, you need to go to the resource file.
**Liudmila Molkova** 39:38 I see.
You know what you're saying, Trask?
**Steve Rao** 39:42 Yeah.
**Trask Stalnaker** 39:44 So maybe for double, it would be double.registry instead of gRPC.target.
**Liudmila Molkova** 39:56 Yeah.
Or a registry address, if there are other important properties.
**Trask Stalnaker** 40:05 Yeah.
And I think the question you're asking, though, is… Should we generalize?
**Liudmila Molkova** 40:16 I… I… I… yes, I'm asking, but I don't think so. I'm just checking if you folks have any… any reference there.
It's like the server address and server port are the unification.
**Steve Rao** 40:38 Yo.
**Trask Stalnaker** 40:42 when there's… When there's no… Yeah, like, it's… it's never gonna be the zookeeper… Or the Nakos.
Server, though, in the server address.
**Liudmila Molkova** 40:58 It could be, right?
**Steve Rao** 41:03 Sorry? Okay, okay, Chaser, can you repeat your question?
**Trask Stalnaker** 41:06 Yeah, so the way I was understanding or reading, like, for gRPC, dot target… That you would capture that if the… has information that's not otherwise captured in server address and server port.
So, which, to me, would mean any… if you have a scheme, any kind of scheme.
**Steve Rao** 41:33 That's additional information that's not in server address and server port.
**Liudmila Molkova** 41:39 Right.
**Trask Stalnaker** 41:42 Oh, I see.
**Liudmila Molkova** 41:43 accuracy.
**Trask Stalnaker** 41:45 She wouldn't… Oh, okay. I see, I'm reading it the other way.
**Liudmila Molkova** 41:56 It's not really the address, but it's the best address we have.
Like, to differ… like, in a sense that it differentiates the endpoints?
But it's not the real.
Address.
**Trask Stalnaker** 42:16 Differentiates the endpoint.
How does that… actually, that's a good question, in that NACOS example… I mean, you're just pointing at a… Like, and so for Zookeeper, also in those Zookeeper examples.
**Steve Rao** 42:43 Zheng Zhu Qing example is similar, just the head is different.
Yeah, it will, reply snuckles by ZoomKeeper. DK.
**Trask Stalnaker** 42:59 But do you know, Ludmila, for gRPC, for example, with the Zookeeper scheme, is there… a service name that you're asking Zookeeper to look up for you?
**Liudmila Molkova** 43:14 No, so that's, like, the combination of those address and port.
So this, this string is everything that's… used.
See, your instances register… That zookeeper, and it knows who is active.
**Trask Stalnaker** 43:39 And the poor.
cluster, every service has its own Zookeeper… Address.
**Liudmila Molkova** 43:51 Yes.
**Trask Stalnaker** 43:52 every logical service that would be balanced across. Okay, okay.
I was… Okay, I was thinking… I was assuming there was, like, a zookeeper Service, and you would ask it for a particular service.
And it would give you one of those. Okay.
So then… It makes… yeah, so then it is at least some… differentiates the services in the way that we… care about.
Okay.
And… Steve, do you know, is that the same as double with, like, Knock goes here… You just ask… Nakos for… You don't tell it which service you want.
**Steve Rao** 44:53 how to understand, you don't tell, which service you want?
**Trask Stalnaker** 45:02 So, the NACOS protocol, you just hit that endpoint, and it gives you one of multiple…
**Steve Rao** 45:14 Yeah, in, in, in double, client. Yeah, it will, it will code the Nugos API.
By pausing the service name.
client want, and the NACOS will have query the related address.
**Liudmila Molkova** 45:39 I see there could be a namespace.
**Steve Rao** 45:43 Yeah, this is a concept in… in… in Nagos.
**Liudmila Molkova** 45:49 So, my, my thinking was that, actually, for, for gRPC, Yeah, like, it's… you can call it full bar.
And you can implement your own resolver that's fullbar. I might even have a full bar resolver, actually.
So… you… Register your resolver and say, okay, you understand what happened with the scheme, and you react to the scheme.
When, you… Or… then you're called… You should do something, and return an arbitrary set of, IP addresses, probably, or some.
Some resolution result with a bunch of addresses.
And however you want to implement it. This, this… Url can be anything. It can contain additional passes, namespaces, and whatnot.
And a very smart instrumentation could understand an arbitrary list of the schemes.
And they can be specific. So, like, for DNS, we know what to do.
Where FUBAR we don't, but we could. We could ask user to configure a specific way to parse server address and port from FUBAR, if that's… what they need.
**Trask Stalnaker** 47:16 Oh, sorry, we've hit our time, but I did… if you can go a little longer, I wanted to follow up on the Zookeep… the gRPC Zookeeper example.
So I'm just, like, you know, asking Copilot random crap, and it's, so it seems like Zookeeper… so it seems like the target could be… like you said, it could have a path on it. It could be server.port and path.
If it has… a path… then… the server… I'm questioning whether we should capture server.address and server.port.
when it's… Zookeeper scheme.
When it's, unknown scheme.
**Liudmila Molkova** 48:09 So, okay, so we know this, we understand DNS, we might have a list of other schemes we don't understand… we understand, and we would parse them.
And for everything else, We would say… no survivor address, no port.
But the gRPC target.
And it will appear on metrics.
And then the typical dashboard would use this story as a… Attribute to the group, son.
**Trask Stalnaker** 48:52 Yeah.
**Liudmila Molkova** 48:54 Okay.
Yeah.
**Trask Stalnaker** 48:57 That makes sense to me.
**Liudmila Molkova** 49:00 And if later on, we would have more clarity on the zookeeper.
I mean, even without it, like, the survey… the method name is… almost… Good enough as a differentiator.
Right.
Only if you have different versions.
**Trask Stalnaker** 49:26 Yeah, but at that point, what's the server.address really?
Anyways… Like, I… I'm a little reluctant to capture server.address to be some, like, registry, like, because server.address Because it's not like we're capturing it as, like, a resource attribute or something higher level, we're capturing it as the span… We're saying this… span… Here's the server.address.
Generally, my… Assumption is that is the address.
that… You know, and it may be a logical address.
But I'm thinking, like, load balance style, like, logical address.
server side. We need a whole new semantic conventions for client load balancing, is the problem.
**Liudmila Molkova** 50:25 That's right.
**Steve Rao** 50:27 Hmm.
Okay, yeah, I want to, yeah, remember another point. At least in Babel, yeah, the communication, with the registry, based on HTTP, such as in Nagos, yeah, maybe the client will… communicate with a registrate, not cause a registrate, by HTTP, so maybe… Yeah, that point, that case, yeah, is not what I should, show in RBC semantic convention.
**Liudmila Molkova** 51:01 Yeah, but then if we get back to… This place, this is the… sorry, my Java hug.
around it. So… The… when the client starts.
**Steve Rao** 51:15 Right?
**Liudmila Molkova** 51:16 Or maybe at some… Period.
the client would resolve the address, or go to zookeeper, go to Nakas, and get the list of endpoints, right?
And it will be notified if something goes wrong with one of them, so it will keep this list up to date. But it's not, like, synchronously, it's not that I'm calling Nakos and then, Going somewhere else.
We're proxying Srinakos.
It's, like, some background stuff that's going on there to resolve.
Mingo.
Yeah.
Okay, I… I think I… I understand your concern, Trask, and I… I agree. I'll update the PR.
**Trask Stalnaker** 52:10 Alright, good discussion.
**Liudmila Molkova** 52:12 Thank you. Thanks for pushing us forward, Linua.
Yeah, thank you both.
**Steve Rao** 52:17 Yeah. Later.
**Trask Stalnaker** 52:18 Sophia?
**Steve Rao** 52:19 See you, bye.
Do you know?
Hmm.
